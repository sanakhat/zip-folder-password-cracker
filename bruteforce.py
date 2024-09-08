from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode())
        print(f"[+] Password found: {password}")
        return True
    except RuntimeError:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip().decode()
                if attempt_extract(zf, password):
                    return
    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
