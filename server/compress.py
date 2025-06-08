import compress_pickle
summarizer = 'summ'

# To save your model with compression
compress_pickle.dump(summarizer, 'model.pkl.lz4', compression='lz4')

# To load it back
model = compress_pickle.load('model.pkl.lz4', compression='lz4')