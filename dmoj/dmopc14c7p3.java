import java.util.*;
import java.io.*;

public class dmopc14c7p3 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static PrintWriter pr = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
        int N = readInt();
        int R = readInt();
        int L = readInt();
        int cnt = 0;

        int[] right = new int[R];
        int[] left = new int[L];

        for(int i = 0; i < R; i++) {
            right[i] = readInt();
        }

        for(int i = 0; i < L; i++) {
            left[i] = readInt();
        }

        Arrays.sort(left);

		for(int i = 0; i < R; i++) {
			if(Arrays.binarySearch(left, right[i]) >= 0) cnt++;
		} 

        System.out.println(N-cnt);
    }
	


	static String next() throws IOException {
		while (st == null || !st.hasMoreTokens())
			st = new StringTokenizer(br.readLine().trim());
		return st.nextToken();
	}

	static long readLong() throws IOException {
		return Long.parseLong(next());
	}

	static int readInt() throws IOException {
		return Integer.parseInt(next());
	}

	static double readDouble() throws IOException {
		return Double.parseDouble(next());
	}

	static char readCharacter() throws IOException {
		return next().charAt(0);
	}

	static String readLine() throws IOException {
		return br.readLine().trim();
	}
}
