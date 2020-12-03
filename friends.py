from mrjob.job import MRJob
class FriendsAvgCount(MRJob):
	def mapper(self,_,line):
		(id,name,age,count)=line.split(',')
		yield age,float(count)
	def reducer(self,age,values):
		a = list(values)
		yield age, sum(a)/ len(a)

if __name__=='__main__':
	FriendsAvgCount.run()

