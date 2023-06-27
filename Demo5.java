package PracticeJava;

public class Demo5{
	public static void main(String[] args) {
		String s1="BOSS";
		String s2=new String("BOSS");
		if(s1==s2)
		{
			System.out.print("Reference are equal");
		}
		else
		{
			System.out.print("Reference are not equal");
		}
		System.out.println();
		
		if(s1.equals(s2))
		{
			System.out.print("Strings are equal");
		}
		else
		{
			System.out.print("Strings are not equal");
		}
		
		
	}

}




