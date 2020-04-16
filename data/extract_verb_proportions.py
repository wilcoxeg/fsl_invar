""" Usage:

cat corpus.conllu | python extract_verb_proportions.py $ANNOTATION_TYPE > output.csv

where $ANNOTATION_TYPE is ud1, ud2, or sud.

"""
import sys
import itertools

import pandas as pd
import cliqs.readcorpora
import cliqs.depgraph as depgraph
import cliqs.conditioning as cond

DEPTYPES = {
    'ud1': {'dobj': 'dobj', 'nsubjpass': 'nsubjpass'},
    'ud2': {'dobj': 'obj', 'nsubjpass': 'nsubj:pass'},
    'sud': {'dobj': 'comp:obj', 'nsubjpass': 'subj@pass'},
}

def instances(deptypes, sentences):
    for s in sentences:
        for n in s.nodes():
            if cond.get_pos(s, n) == 'VERB':
                out_types = [
                    dt['deptype'] for _, _, dt in s.out_edges(n, data=True)
                ]
                yield {
                    'word': cond.get_word(s, n).lower(),
                    'lemma': cond.get_lemma(s, n).lower(),
                    'ptb_pos': cond.get_pos2(s, n),
                    'has_dobj': deptypes['dobj'] in out_types,
                    'has_nsubjpass': deptypes['nsubjpass'] in out_types,
                }

def run(annotation_type, sentences):
    the_instances = pd.DataFrame(instances(DEPTYPES[annotation_type], sentences))
    counts = the_instances.groupby(list(the_instances.columns)).size().reset_index(name='count')
    return counts

def main(annotation_type='ud1'):
    assert annotation_type in set(DEPTYPES.keys()), "Annotation type argument must be in %s" % str(set(DEPTYPES.keys()))
    sentences = cliqs.readcorpora.UniversalDependency1Treebank().sentences() # reads from stdin    
    result = run(annotation_type, sentences)
    result.to_csv(sys.stdout)
    return 0

if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
