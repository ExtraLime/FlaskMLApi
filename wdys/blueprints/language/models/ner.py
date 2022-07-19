#!/usr/bin/python3
import pathlib
from transformers import pipeline


path = pathlib.Path(__file__).parent.resolve()
full_path = str(path)+'/entity'

nlp = pipeline(task='token-classification',
               tokenizer=full_path,
               model=full_path)


class NER:
    def __init__(self) -> None:
        self.model = nlp

    def get_ents(self, input_string: str = ''):
        raw_result = self.model(input_string)

        entities = []

        for i in range(len(raw_result)):
            if i > 0 and raw_result[i]['word'].startswith('##'):
                entities[-1] = {raw_result[i-1]['word']+raw_result[i]
                                ['word'].replace('##', ''):
                                    raw_result[i]['entity']}
            else:
                entities.append(
                    {raw_result[i]['word']: raw_result[i]['entity']})

        return entities


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--sentence', type=list)

    args = parser.parse_args()
    sent = ''.join(args.sentence)
    NER = NER()
    ner = NER.get_ents(input_string=sent)
    print(ner)
