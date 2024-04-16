
Today we’re going to analyse TV shows to get their average episode rating and a list of their best-rated episodes. We will use data from IMDb (the same as Lab 4), which look like:

The columns are: (1) the number of votes, (2) the average vote, (3) the series name, (4) the series year, (5) the type,
(6) the name of the episode. Where column (6) is null for a TV series, the voting information is the overall for the
series (on IMDb, one can vote on the series page or on an individual episode). The data are on the HDFS storage of
the cluster: hdfs://cm:9000/uhadoop/shared/imdb/imdb-ratings.tsv. We want to compute output tuples of the form:

TheWire#2002 -30- (#5.10)|Middle Ground (#3.11) 9.6 8.583

Where the columns are: (1) a key for the series (name#year), (2) a list of episodes tied for best rating using ‘|’
as a delimiter, (3) the best rating of an episode (and thus the ratings of episodes in (2)), (4) the average rating of all
episodes (excluding the series value, e.g., the first line in the input above)

We will use Spark for processing. For testing, hdfs://cm:9000/uhadoop/shared/imdb/imdb-ratings-two.tsv is
a small example file with two series and an irrelevant movie you should filter; one of the series is The Wire (2002),whose
results should correspond to the those indicated above (modulo some minor rounding differences). Note that the actual
output given by Spark will use commas and brackets rather than tabs, which is fine: the syntax of the lines is not
important, but rather we care about the content of each line. Also be aware that Spark will often include
multiple output files of the type part-NNNNN in the output folder; all of these form part of the output. (You
can use “part-*” in combination with cat to concatenate the different output parts, where * acts as a wildcard.)
There are multiple options with which to run Spark, including Java, Scala, Python and R. Of these options, both
Java and Scala can be considered “native” as – like Spark – they run in the Java Virtual Machine (JVM). The server
we will use can run Java, Scala and Python. You can submit the work in Java, Scala or Python.

Now to the main task: your goal is to use Spark Core to output for each series, (1) the average episode rating,
(2) the best episode rating, and (3) the names of episodes with the best rating, as per the example in the
introduction. You need to copy the AverageSeriesRating file in the language of your choice to a new file called
InfoSeriesRating and start extending it to look for info on the best episodes. In so doing, you should follow
the example of AverageSeriesRating, reading the input from HDFS and writing the output to HDFS. You
should test this on the small example provided before running it on the full file. In the case of Python and Scala,
we highly recommend developing the new script line-by-line in the respective shell, revising the output as you
proceed over the example. You should also ensure to cache any RDDs you use more than once. Please see the
example output in the introduction for The Wire#2002 for the task you need to build; again note that is not
necessary to have the exact syntax shown for each line, just the correct information on each line.
 Once your code is ready and working on the small file, you should run it on the full ratings data found in
hdfs://cm:9000/uhadoop/shared/imdb/imdb-ratings.tsv and revise the results.

## Java snippets 

This is an optional guide to help you code your solution in Java. You should start by copying the class called AverageSeriesRating.java to the same package with the name InfoSeriesRating.java. The code given to you in
AverageSeriesRating.java computes the average rating of episodes in a series, which you should extend with the
information about the names of the best-rated episodes and their rating. You can extend the given code with the
following snippets to complete the lab. Snippets may be out of order but are sufficient to complete the lab. Note that:

- You will need to change the names of rdd1, rdd2 and rdd3 (the new names might be different every time;
some RDD names might already appear in the code of AverageSeriesRating.java).
- You may need to modify parts of the code already given to you in AverageSeriesRating.java.
- You may also need to change the name of the RDD that you store to HDFS towards the end of the code.
- Where you see a question mark “?”, this means that you need to fill the slot with some code.

**Cache**: This caches the RDD rdd2 as rdd1 in order to use it multiple times without recomputing it from scratch
each time. You should henceforth refer to rdd1 rather than rdd2 to avoid the re-computation. Note that this might require modifying code already given in AverageSeriesRating.java.

```Java 
JavaRDD<Tuple3><String, String, Double>> rdd1 = rdd2.cache();
```

**Map-to-pair**: This creates a `PairRDD rdd1` from `rdd2` 

```Java 
JavaPairRDD<String,Tuple2<String,Double>> rdd1 = rdd2.mapToPair(

?

);
```

**Reduce-by-key**: This creates a new `RDD rdd1` resulting from a reduce-by-key on `rdd2`-  

```Java 
JavaPairRDD<String,Tuple2<String,Double>> rdd1 = rdd2.reducebyKey(

?

);
```
**Join**: This creates a new RDD `rdd1`resulting from a join on `rdd2` and `rdd3`. 

```Java 
JavaPairRDD<String, Tuple2<Tuple2<String, Double>, Double>> rdd1 = rdd2.join(rdd3);
```

**First lambda**: This creates pairs of the form $(s_1, (s_2, d))$ from triples $(s_1, s_2, d)$ with $s_1, s_2$, strings, and $d$ a double. 

```Java 
tup -> new Tuple2<String,Tuple2<String,Double>>(tup._1(),new Tuple2<String,Double>(tup._2(),tup._3()))
```

**Second lambda**: This lambda collects a maximum value and a list of names of elements with the maximum value. 

```Java 
(a, b) ->
	{ if(a._2 > b._2) return a;
		else if(b._2 > a._2) return b;
		return new Tuple2<String, Double>(a._1 + "|" + b._1, a._2);
	}
```

## Sample code 

```Java 
package org.mdp.spark.cli;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;

import scala.Tuple2;
import scala.Tuple3;

/**
 * Get the average ratings of TV series from IMDb.
 * 
 * This is the Java 8 version with lambda expressions.
 */
public class AverageSeriesRating {
	/**
	 * This will be called by spark
	 */
	public static void main(String[] args) {
		
		if(args.length != 2) {
			System.err.println("Usage arguments: inputPath outputPath");
			System.exit(0);
		}
		new AverageSeriesRating().run(args[0],args[1]);
	}

	/**
	 * The task body
	 */
	public void run(String inputFilePath, String outputFilePath) {
		/*
		 * Initialises a Spark context with the name of the application
		 *   and the (default) master settings.
		 */
		SparkConf conf = new SparkConf()
				.setAppName(AverageSeriesRating.class.getName());
		JavaSparkContext context = new JavaSparkContext(conf);

		/*
		 * Load the first RDD from the input location (a local file, HDFS file, etc.)
		 */
		JavaRDD<String> inputRDD = context.textFile(inputFilePath);
		
		/*
		 * Here we filter lines that are not TV series or where no episode name is given
		 */
		JavaRDD<String> tvSeries = inputRDD.filter(
				line -> line.split("\t")[4].equals("tvSeries") && !line.split("\t")[5].equals("null")
		);
		
		/*
		 * We create a tuple (series,episode,rating) where series is the key (name+"#"+year+"#"+disambiguator)
		 */
		JavaRDD<Tuple3<String,String,Double>> seriesEpisodeRating = tvSeries.map(
				line -> new Tuple3<String,String,Double> (
							line.split("\t")[2] + "#" + line.split("\t")[3],
							line.split("\t")[5],
							Double.parseDouble(line.split("\t")[1])
						)
		);
		
		/*
		 * Now we start to compute the average rating per series.
		 * 
		 * We don't care about the episode name for now so to start with, 
		 * from tuples (series,episode,rating)
		 * we will produce a map: (series,rating)
		 * 
		 * (We could have done this directly from tvSeries, 
		 *   except seriesEpisodeRating will be reused later)
		 */
		JavaPairRDD<String,Double> seriesToEpisodeRating = seriesEpisodeRating.mapToPair(
				tup -> new Tuple2<String,Double> (
							tup._1(),
							tup._3()
						)
		);
		
		/*
		 * To compute the average rating for each series, the idea is to
		 * maintain the following tuples:
		 * 
		 * (series,(sum,count))
		 * 
		 * Where series is the series identifier, 
		 *   count is the number of episode ratings thus far
		 *   sum is the sum of episode ratings thus far
		 *
		 * Base value: (0,0)
		 *
		 * To combine (sum, count) | rating:
		 *   (sum+rating,count+1)
		 *   
		 * To reduce (sum1,count1) | (sum2,count2)
		 *   (sum1+sum2,count1+count2)
		 */
		JavaPairRDD<String, Tuple2<Double, Integer>> seriesToSumCountRating = 
				seriesToEpisodeRating.aggregateByKey(
						new Tuple2<Double, Integer>(0d, 0), // base value
						(sumCount, rating) -> 
							new Tuple2<Double, Integer>(sumCount._1 + rating, sumCount._2 + 1 ), // combine function
						(sumCountA, sumCountB) -> 
							new Tuple2<Double, Integer>(sumCountA._1 + sumCountB._1, sumCountA._2 + sumCountB._2 )); // reduce function
		
		/*
		 * Given final values for:
		 * 
		 * (series,(sum,count))
		 * 
		 * Create the average:
		 * 
		 * (series,sum/count)
		 */
		JavaPairRDD<String,Double> seriesToAvgRating = seriesToSumCountRating.mapToPair(
				tup -> new Tuple2<String,Double>(tup._1,tup._2._1/tup._2._2)
		);
		
		/*
		 * Write the output to local FS or HDFS
		 */
		seriesToAvgRating.saveAsTextFile(outputFilePath);
		
		context.close();
	}
}
```

