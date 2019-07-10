//Constant interface antipattern. Don't do it !
public interface PhysicalConstants {
	static final double AVOGADROS_NUMBER = 6.022_140_857e23;
	static final double BOLTZMAN_CONSTANT = 1.380_648_52e-23;
	...
}
//Instead use
public class PhysicalConstants {
	private PhysicalConstants() {} //prevents instatiation
	
	public static final double AVOGADROS_NUMBER = 6.022_140_857e23;
	public static final double BOLTZMAN_CONSTANT = 1.380_648_52e-23;
	...
}