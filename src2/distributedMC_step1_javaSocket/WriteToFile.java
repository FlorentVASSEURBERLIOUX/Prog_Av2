package assignments;

import java.io.FileWriter;
import java.io.IOException;

public class WriteToFile {
	public static void put(String data, String file) {
		try {
			FileWriter writer = new FileWriter("../tests/" + file,true);
			writer.append(data);
			writer.close();
			System.out.println("Successfully wrote text to file.");
			System.out.println(data);
		} catch (IOException e) {
			System.out.println("An error occurred.");
			e.printStackTrace();
		}
    }
}
