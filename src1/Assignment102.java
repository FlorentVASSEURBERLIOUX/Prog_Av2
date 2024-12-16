// Estimate the value of Pi using Monte-Carlo Method, using parallel program
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
		int[] totalCounts = {64000000,128000000};
		int[] numWorkersList = {8};
		int repeat_code = 10;

		for (int totalCount : totalCounts) {
			for (int numWorkers : numWorkersList) {
				System.out.println("Running simulation with totalCount = " + totalCount + " and numWorkers = " + numWorkers);
				for (int i = 0; i < repeat_code; i++) {
					Assignment102.execute(totalCount, numWorkers);
				}
			}
		}
	}

	private static void execute(int totalP, int Nproc){
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

