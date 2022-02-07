// Anti Debugging bypass script

// ptrace bypass
Interceptor.attach(Module.findExportByName(null, 'ptrace'), {
    onEnter: function(args) {
        console.log("[*] ptrace called !");
        if(args[0].toInt32() == 31) {
            console.log("ptrace Anti Debugging Bypass !");
            args[0] = ptr(0x0);
        }
    }
})

// SVC call ptrace bypass
// var m = Process.findModuleByName('ModuleName');
// var pattern = '50 03 80 D2 01 10 00 D4';
// Memory.scan(m.base, m.size, pattern, {
// 	onMatch: function(address, size) {
// 		console.log('[*] SVC call Anti Debugging Bypass !');
// 		console.log(Memory.readByteArray(address, size));
// 		Memory.protect(address, size, 'rwx');
// 		Memory.writeByteArray(address.add(4), [0x1F, 0x20, 0x03, 0xD5]);
// 		console.warn(Memory.readByteArray(address, size));
// 	},
// 	onComplete: function () {
// 		console.log("[*] SVC call ptrace Anti Debugging Bypass !");
// 	}
// })

// sysctl bypass
Interceptor.attach(Module.findExportByName(null, 'sysctl'), {
	onEnter: function(args) {
		this.kp_proc = args[2];
		this.count = args[1];
	},
	onLeave: function(retval) {
		if(retval == 0x0) {
			if(this.count.toInt32() == 4) {
				var p_flag = Memory.readInt(this.kp_proc.add(32));
					if((p_flag & 0x800) !== 0) {
						console.log('[*] sysctl Anti Debugging Bypass !');
						Memory.writeByteArray(this.kp_proc.add(32), [0x00, 0x00]);
					}
			}
		}
	}
});

// getppid bypass
Interceptor.attach(Module.findExportByName(null, 'getppid'), {
	onEnter: function(args) {
	},
	onLeave: function(retval) {
		console.log("[*] getppid Anti Debugging Bypass !");
		retval.replace(ptr("0x1"));
	}
});