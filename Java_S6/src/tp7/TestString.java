package tp7;

public class TestString {

    public static void main(String[] args) {
        String s = "Hello";
        StringBuilder sb = new StringBuilder();
        sb.append("Hello");
        System.out.println(s.equals(sb.toString()));
    }
}
