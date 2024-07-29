package security;

import java.io.Console;

public class Security{

    final static int MOD = 256;
    String passkey;

    public Security(){
        this.passkey = "";
    }

    static Character getValueForCurrentChar(Character a, Character b, boolean isEncrypting){
        if(isEncrypting)
            return (char) (((int) a + (int) b) % MOD);
        else
            return (char) (((int) a - (int) b) % MOD);
    }

    public String encrypt(String messageString){
        StringBuilder encryptedString = new StringBuilder();

        int passKeyIndex = 0;
        for(int i = 0; i < messageString.length(); i++){
            encryptedString.append(getValueForCurrentChar(messageString.charAt(i), passkey.charAt(passKeyIndex), true));
            passKeyIndex = (passKeyIndex + 1) % passkey.length();
        }

        return encryptedString.toString();
    }

    public String decrypt(String messageString){
        StringBuilder decryptedString = new StringBuilder();

        int passKeyIndex = 0;
        for(int i = 0; i < messageString.length(); i++){
            decryptedString.append(getValueForCurrentChar(messageString.charAt(i), passkey.charAt(passKeyIndex), false));
            passKeyIndex = (passKeyIndex + 1) % passkey.length();
        }
        return decryptedString.toString();
    }

    public void setPassKey(String passKey){
        this.passkey = passKey;
    }

    public void setPassKey(){
        Console console = System.console();
        if(console != null){
            this.passkey = console.readLine("Enter your passkey: ");
        }
        return;
    }

    public static void main(String[] args) {
        Security security = new Security();
        String message = "Hello, World!";
        String passkey = "secret";
        security.setPassKey(passkey);
        String encrypted = security.encrypt(message);
        System.out.println(encrypted);
        System.out.println(security.decrypt(encrypted));

    }
}


// A map which would have characters associated with keys
//