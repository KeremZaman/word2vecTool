__author__ = 'Kerem'
import gensim,string,argparse,sys

class Feeder():
	def __init__(self,path):
		self.file = path
	
	def __iter__(self):
		with open(self.file,'r') as f:
			for line in f.readlines():
				yield line.strip()


class VectorCreator():
	def __init__(self,input,output,workers,size):
		self.workers = workers
		self.size = size
		if input is None:
			input = 'preprocessed.txt'
		self.sentences = Feeder(input)
		if output is None:
			output = 'model'
		self.output = output

	def create(self):
		model = gensim.models.Word2Vec(self.sentences,size = self.size, workers = self.workers)
		model.save(self.output)
	

class Preprocessor():
	def __init__(self,input,output=None):
		rmv = string.punctuation + '‘’“”' # can be extended. need update for opennmt seperators
		self.translator = str.maketrans('','',rmv)
		self.input = input
		if output:
			self.output = output
		else:
			self.output = 'preprocessed.txt'
	
	def write_file(self,line):
		with open(self.output,'a') as f:
			print(line,file=f)
			
	def preprocess(self):
		f = Feeder(self.input)
		for line in f:
			self.write_file(line.translate(self.translator).lower()) # do sth for repeating spaces
			
class Runner():
	def __init__(self,args):
		self.input = args.input
		self.run(args)
		
	def run(self,args):
		if args.only_preprocess:
			p = Preprocessor(self.input,args.only_preprocess)
			p.preprocess()
		
		elif args.only_train:
			vc = VectorCreator(args.input,args.only_train,args.workers,args.size)
			vc.create()
		
		else:
			p = Preprocessor(self.input)
			p.preprocess()
			vc = VectorCreator(args.input,args.model,args.workers,args.size)
			vc.create()
			

def main(arguments):
	parser = argparse.ArgumentParser(
		description=__doc__,
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--input', help="Input to generate vectors (raw file for default, preprocessed file for only-train mode )", required = True, type = str)
	parser.add_argument('--model', help="Name for model", required = False, type = str, default = 'model')
	parser.add_argument('--workers', help="Workers for training (default:4)", required = False, type = int, default = 4)
	parser.add_argument('--size', help="Dimension of vectors (default:300)", required = False, type = int, default = 300)
	parser.add_argument('--only-preprocess', help="Only preprocess input file, enter name for output", required = False, type=str)
	parser.add_argument('--only-train', help="Only train preprocessed input file, enter name for output", required = False, type=str)
	args = parser.parse_args(arguments)
	if args.input:
		r = Runner(args)

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
