{
    "variables": {
        'node_shared_openssl%': 'true'
    },
    "targets": [
    {
        "target_name": "brypt-crypto",
        'cflags!': [ '-fno-exceptions' ],
        'cflags_cc!': [ '-fno-exceptions' ],
        "sources": [
            "./src/crypto/crypto.cpp",
        ],
        'conditions': [
            [ 'OS=="win"', {
                'conditions': [
                    ['target_arch=="x64"', {
                        'variables': {
                        'openssl_root%': 'C:/OpenSSL-Win64/openssl-1.1.0f-vs2017'
                    },
                    }, {
                        'variables': {
                            'openssl_root%': 'C:/OpenSSL-Win32'
                        },
                    }],
                ],
                'defines': [
                    'uint=unsigned int',
                ],
                'libraries': [
                    '-l<(openssl_root)/lib64/libcryptoMT.lib',
                    '-l<(openssl_root)/lib64/libsslMT.lib',
                ],
                'include_dirs': [
                    "<!(node -e \"require('nan')\")",
                    "<(openssl_root)/include64/openssl",
                    "<(openssl_root)/include64",
                ],
            }, { # OS!="win"
                'libraries': [
                    "-L/usr/local/lib",
                    "-L/usr/local/include/openssl",
                    "/usr/local/lib/libcrypto.a",
                    "-lcrypto",
                ],
                'include_dirs': [
                    "<!(node -e \"require('nan')\")",
                    "/usr/local/include/openssl",
                    "/usr/local/include/openssl/openssl",
                ],
            }],
            ['OS=="mac"', {
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                    "OTHER_CFLAGS": [
                        "-std=c++11",
                        "-stdlib=libc++",
                        "-Wall"
                    ]
                }
            }],
            ['OS=="linux"', {
                "OTHER_CFLAGS": [
                    "-std=c++11",
                    "-stdlib=libc++",
                    "-Wall" 
                ]
            }],
            ['OS=="win"', {
                "OTHER_CFLAGS": [
                    "-std=c++11",
                    "-stdlib=libc++",
                    "-Wall"
                ]
            }]
        ],
    },
    {
        "target_name": "brypt-message",
        'cflags!': [ '-fno-exceptions' ],
        'cflags_cc!': [ '-fno-exceptions' ],
        "sources": [
            "./src/message/addon.cpp",
            "./src/message/message.cpp",
        ],
        "include_dirs": [
            "<!@(node -p \"require('node-addon-api').include\")"
        ],
        'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
        'conditions': [
            [ 'OS=="win"', {
                'conditions': [
                    ['target_arch=="x64"', {
                        'variables': {
                        'openssl_root%': 'C:/OpenSSL-Win64/openssl-1.1.0f-vs2017'
                    },
                    }, {
                        'variables': {
                            'openssl_root%': 'C:/OpenSSL-Win32'
                        },
                    }],
                ],
                'defines': [
                    'uint=unsigned int',
                ],
                'libraries': [
                    '-l<(openssl_root)/lib64/libcryptoMT.lib',
                    '-l<(openssl_root)/lib64/libsslMT.lib',
                ],
                'include_dirs': [
                    "<!(node -e \"require('nan')\")",
                    "<(openssl_root)/include64/openssl",
                    "<(openssl_root)/include64",
                ],
            }, { # OS!="win"
                'libraries': [
                    "-L/usr/local/lib",
                    "-L/usr/local/include/openssl",
                    "/usr/local/lib/libcrypto.a",
                    "-lcrypto",
                    # "-lssl"
                ],
                'include_dirs': [
                    "<!(node -e \"require('nan')\")",
                    "/usr/local/include/openssl",
                    "/usr/local/include/openssl/openssl",
                ],
            }],
            ['OS=="mac"', {
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                    "OTHER_CFLAGS": [
                        "-std=c++11",
                        "-stdlib=libc++",
                        "-Wall"
                    ]
                }
            }],
            ['OS=="linux"', {
                "OTHER_CFLAGS": [
                    "-std=c++11",
                    "-stdlib=libc++",
                    "-Wall"
                ]
            }],
            ['OS=="win"', {
                "OTHER_CFLAGS": [
                    "-std=c++11",
                    "-stdlib=libc++",
                    "-Wall"
                ]
            }]
        ],
    }]
}
