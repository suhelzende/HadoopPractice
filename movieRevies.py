from mrjob.job import MRJob
from mrjob.step import MRStep
class MRRatingCounter(MRJob):
	def mapper(self, key, line):
		(userid, movieId, rating, timestamp)= line.split("\t")
		yield rating, 1

	def reducer(self, rating, values):
		yield  rating, sum(values)

#	def steps(self):
#		return [MRStep(mapper=self.mapper,reducer=self.reducer)]

if __name__=='__main__':
	MRRatingCounter.run()
