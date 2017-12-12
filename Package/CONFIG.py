import ops
import iopc

pkg_path = ""
output_dir = ""
arch = ""
src_usr_lib_dir = ""
src_usr_bin_dir = ""
dst_lib_dir = ""
dst_usr_bin_dir = ""
src_include_dir = ""
dst_include_dir = ""

def set_global(args):
    global pkg_path
    global output_dir
    global arch
    global src_usr_lib_dir
    global src_usr_bin_dir
    global dst_lib_dir
    global dst_usr_bin_dir
    global src_include_dir
    global dst_include_dir
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    arch = ops.getEnv("ARCH_ALT")
    if arch == "armhf":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/arm-linux-gnueabihf")
        src_usr_bin_dir = iopc.getBaseRootFile("usr/bin")
    elif arch == "armel":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/arm-linux-gnueabi")
        src_usr_bin_dir = iopc.getBaseRootFile("usr/bin")
    elif arch == "x86_64":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/x86_64-linux-gnu")
        src_usr_bin_dir = iopc.getBaseRootFile("usr/bin")
    else:
        sys.exit(1)
    dst_lib_dir = ops.path_join(output_dir, "lib")
    dst_usr_bin_dir = ops.path_join(output_dir, "usr/bin")

    src_include_dir = iopc.getBaseRootFile("usr/include/luajit-2.0")
    dst_include_dir = ops.path_join("include",args["pkg_name"])


def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    if False :
        ops.mkdir(dst_usr_bin_dir)
        ops.copyto(ops.path_join(src_usr_bin_dir, "luajit-2.0.4"), dst_usr_bin_dir)
        ops.ln(dst_usr_bin_dir, "luajit-2.0.4", "luajit")
        
        ops.mkdir(dst_lib_dir)
        ops.copyto(ops.path_join(src_usr_lib_dir, "libluajit-5.1.so.2.0.4"), dst_lib_dir)
        ops.ln(dst_lib_dir, "libluajit-5.1.so.2.0.4", "libluajit-5.1.so.2.0")
        ops.ln(dst_lib_dir, "libluajit-5.1.so.2.0.4", "libluajit-5.1.so.2")
        ops.ln(dst_lib_dir, "libluajit-5.1.so.2.0.4", "libluajit-5.1.so")
        ops.ln(dst_lib_dir, "libluajit-5.1.so.2.0.4", "liblua5.1.so.0")
        ops.ln(dst_lib_dir, "libluajit-5.1.so.2.0.4", "liblua5.1.so")

    ops.mkdir(dst_lib_dir)
    ops.copyto(ops.path_join(src_usr_lib_dir, "liblua5.1.so.0.0.0"), dst_lib_dir)
    ops.ln(dst_lib_dir, "liblua5.1.so.0.0.0", "liblua5.1.so.0.0")
    ops.ln(dst_lib_dir, "liblua5.1.so.0.0.0", "liblua5.1.so.0")
    ops.ln(dst_lib_dir, "liblua5.1.so.0.0.0", "liblua5.1.so")
    #ops.mkdir(dst_include_dir)
    #iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "lauxlib.h"), dst_include_dir)
    #iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "lua.h"), dst_include_dir)
    #iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "luaconf.h"), dst_include_dir)
    #iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "luajit.h"), dst_include_dir)
    #iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "lualib.h"), dst_include_dir)
    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(build_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)
    return False

def MAIN_BUILD(args):
    set_global(args)
    return False

def MAIN_INSTALL(args):
    set_global(args)

    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "lauxlib.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "lua.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "luaconf.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "luajit.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "lualib.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(dst_lib_dir, "."), "lib") 
    #iopc.installBin(args["pkg_name"], ops.path_join(dst_usr_bin_dir, "."), "usr/bin") 
    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)
    return False

def MAIN(args):
    set_global(args)

