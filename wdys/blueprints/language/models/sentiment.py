#!/usr/bin/python3
import pathlib
from transformers import pipeline

path = pathlib.Path(__file__).parent.resolve()
full_path = str(path)+'/sentiment'

nlp = pipeline(task='text-classification',
               model=full_path, tokenizer=full_path)


class SA:
    def __init__(self) -> None:
        self.model = nlp

    def get_sentiment(self, input_string: str = ''):
        raw_result = self.model(input_string)

        return raw_result


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('sentence', type=list)

    args = parser.parse_args()
    sent = ' '.join(args.sentence)
    sa = SA()
    result = SA.get_sentiment(input_string=sent)
    print(result)
