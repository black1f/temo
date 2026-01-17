import os, sys, platform, time

# إضافة المسار الحالي لضمان رؤية الملف المشفر
sys.path.append(os.path.abspath(os.getcwd()))

def run_tool():
    os.system('clear')
    print(f'\x1b[1;97m[•] YOUR DEVICE IS {platform.architecture()[0]}')
    time.sleep(1)
    
    try:
        # استدعاء الملف المشفر
        import sh_corrected
        # تشغيل الكلاس الرئيسي
        sh_corrected.__ERRORJO__().__MENU__()
    except ImportError:
        print('\x1b[1;91m[!] Error: Encrypted file (sh_corrected.so) not found!\x1b[1;97m')
    except Exception as e:
        print(f'\x1b[1;91m[!] Error: {e}\x1b[1;97m')

if __name__ == '__main__':
    run_tool()
