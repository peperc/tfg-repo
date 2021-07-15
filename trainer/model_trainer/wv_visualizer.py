if __name__ == '__main__':

    import sys
    import io
    from gensim.models import KeyedVectors
    
    
    if len(sys.argv) == 2:

        # Load gensim word2vec
        w2v = KeyedVectors.load(sys.argv[1])

        
        # Vector file, `\t` seperated the vectors and `\n` seperate the words
        """
        0.1\t0.2\t0.5\t0.9
        0.2\t0.1\t5.0\t0.2
        0.4\t0.1\t7.0\t0.8
        """
        out_v = io.open('models/vecs.tsv', 'w', encoding='utf-8')


        # Meta data file, `\n` seperated word
        """
        token1
        token2
        token3
        """
        out_m = io.open('models/meta.tsv', 'w', encoding='utf-8')


        # Write meta file and vector file
        for index in range(len(w2v.index_to_key)):
            word = w2v.index_to_key[index]
            vec = w2v.vectors[index]
            out_m.write(word + "\n")
            out_v.write('\t'.join([str(x) for x in vec]) + "\n")
            out_v.close()
            out_m.close()

        # Then we can visuale using the `http://projector.tensorflow.org/` to visualize those two files.
        # 1. Open the Embedding Projector.
        # 2. Click on "Load data".
        # 3. Upload the two files we created above: vecs.tsv and meta.tsv.