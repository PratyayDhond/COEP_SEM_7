import java.io.*;
import java.net.*;
import security.Security;

class Server{
  public static void main(String[] args) throws Exception{
    System.out.println("--------------------Server Program-------------------- \n");
    ServerSocket ss = new ServerSocket(2003);
    Socket s = ss.accept();
    String passkey = "qwertyxz123";

    DataInputStream din = new DataInputStream(s.getInputStream());
    DataOutputStream dos =new DataOutputStream(s.getOutputStream());

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str1="",str2="";

    Security security = new Security();
    security.setPassKey();

    while(!str2.equals("-1")){
      str1 = security.decrypt(din.readUTF());
      if(!str1.equals("-1"))
        System.out.println("C: " + str1);
      else{
      	dos.writeUTF(security.encrypt("-1"));
      	break;  
      }
      System.out.print("> ");
      str2 = br.readLine();
      dos.writeUTF(security.encrypt(str2));
    }

    dos.close();
    din.close();
    ss.close();
    s.close();
    System.out.println("Server disconnected successfully");
  }
}