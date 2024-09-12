{
    'targets': [
        {
            'target_name': 'casclib-native',
            'sources': [
                'src/errors.cc',
                'src/locales.cc',
                'src/storageinfo.cc',
                'src/storage.cc',
                'src/find.cc',
                'src/openfile.cc',
                'src/readfile.cc',
                'src/casclib.cc',
            ],
            'include_dirs': [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            'dependencies': [
                "<!(node -p \"require('node-addon-api').gyp\")",
                "CascLibRAS"
            ],
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ],
            'xcode_settings': {
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                'CLANG_CXX_LIBRARY': 'libc++',
                'MACOSX_DEPLOYMENT_TARGET': '10.7'
            },
            'msvs_settings': {
                'VCCLCompilerTool': {
                    'ExceptionHandling': 1,
                },
            }
        },
        {
            'target_name': "CascLibRAS",
            'type': 'static_library',
            'include_dirs': [
                "CascLib/src/",
            ],
            'sources': [
                'CascLib/src/CascDecrypt.cpp',
                'CascLib/src/CascFiles.cpp',
                'CascLib/src/CascDecompress.cpp',
                'CascLib/src/CascDumpData.cpp',
                'CascLib/src/CascFindFile.cpp',
                'CascLib/src/CascIndexFiles.cpp',
                'CascLib/src/CascOpenFile.cpp',
                'CascLib/src/CascOpenStorage.cpp',
                'CascLib/src/CascReadFile.cpp',
                'CascLib/src/CascRootFile_Diablo3.cpp',
                'CascLib/src/CascRootFile_Install.cpp',
                'CascLib/src/CascRootFile_MNDX.cpp',
                'CascLib/src/CascRootFile_OW.cpp',
                'CascLib/src/CascRootFile_Text.cpp',
                'CascLib/src/CascRootFile_TVFS.cpp',
                'CascLib/src/CascRootFile_WoW.cpp',
                'CascLib/src/common/Common.cpp',
                'CascLib/src/common/Directory.cpp',
                'CascLib/src/common/Csv.cpp',
                'CascLib/src/common/FileStream.cpp',
                'CascLib/src/common/FileTree.cpp',
                'CascLib/src/common/ListFile.cpp',
                'CascLib/src/common/RootHandler.cpp',
                'CascLib/src/common/Mime.cpp',
                'CascLib/src/common/Sockets.cpp',
                'CascLib/src/hashes/sha1.cpp',
                'CascLib/src/jenkins/lookup3.c',
                'CascLib/src/hashes/md5.cpp',
                'CascLib/src/overwatch/aes.cpp',
                'CascLib/src/overwatch/apm.cpp',
                'CascLib/src/overwatch/cmf.cpp',
                'CascLib/src/zlib/adler32.c',
                'CascLib/src/zlib/crc32.c',
                'CascLib/src/zlib/deflate.c',
                'CascLib/src/zlib/inffast.c',
                'CascLib/src/zlib/inflate.c',
                'CascLib/src/zlib/inftrees.c',
                'CascLib/src/zlib/trees.c',
                'CascLib/src/zlib/zutil.c',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    "CascLib/src",
                ]
            }
        },
  ]
}
