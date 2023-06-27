package PracticeJava;

public class Demo7 {
	public static void main(String[] args) {
		String s1="OM";
		String S2="KAR";
		String s3="OM" + "KAR";
		String s4="OM" + "KAR";
		if(s3==s4)
		{
			System.out.println("Reference are equal");
		}
		else
		{
			System.out.println("Reference are not equal");
			
	}
		if(s3.equals(s4))
		{
			System.out.println("Strings are equal");
		}
		else
		{
			System.out.println("Strings are not equal");
			
	}
		
	}

}
