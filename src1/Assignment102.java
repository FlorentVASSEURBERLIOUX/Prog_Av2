// Estimate the value of Pi using Monte-Carlo Method, using parallel program
package assignments;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;
class PiMonteCarlo {
	AtomicInteger nAtomSuccess;
	int nThrows;
	double value;
	int nProcessors;
	class MonteCarlo implements Runnable {
		@Override
		public void run() {
			double x = Math.random();
			double y = Math.random();
			if (x * x + y * y <= 1)
				nAtomSuccess.incrementAndGet();
		}
	}
	public PiMonteCarlo(int i, int proc) {
		this.nAtomSuccess = new AtomicInteger(0);
		this.nThrows = i;
		this.value = 0;
		this.nProcessors = proc;
	}
	public double getPi() {
		ExecutorService executor = Executors.newWorkStealingPool(nProcessors);
		for (int i = 1; i <= nThrows; i++) {
			Runnable worker = new MonteCarlo();
			executor.execute(worker);
		}
		executor.shutdown();
		while (!executor.isTerminated()) {
		}
		value = 4.0 * nAtomSuccess.get() / nThrows;
		return value;
	}
	public double getNbSuccesPoint() {
		return nAtomSuccess.get();
	}

}

public class Assignment102 {
	public static void main(String[] args) {
		int totalP = 100000;
		int Nproc = 1;
		PiMonteCarlo PiVal = new PiMonteCarlo(totalP,Nproc);
		long startTime = System.currentTimeMillis();
		double value = PiVal.getPi();
		long stopTime = System.currentTimeMillis();
		System.out.println("\nPi : " + value );
		System.out.println("Error: " + (Math.abs((value - Math.PI)) / Math.PI) +"\n");

		System.out.println("Ntot: " + totalP);
		System.out.println("Available processors: " + PiVal.nProcessors);
		System.out.println("Time Duration (ms): " + (stopTime - startTime) + "\n");

		System.out.println("total from Master = " + PiVal.getNbSuccesPoint());
		WriteToFile.put((Math.abs((value - Math.PI)) / Math.PI) +";"+ totalP +";"+ value +";"+ PiVal.getNbSuccesPoint() +";"+ (stopTime - startTime) +";"+ Nproc+"\n", "Assignement102.txt");
	}
}

