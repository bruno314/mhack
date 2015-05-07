import subprocess

__author__ = 'bruno'
import Quandl
import json
import pandas as pd
import math
import os

class routine():
    @staticmethod
    def get_bitcoin_price():
        val = single.get("BAVERAGE/CNY", target="Pandas")
        assert isinstance(val, pd.DataFrame)
        bitcoin_price = list(val["24h Average"])
        return list(map(math.floor, bitcoin_price))

    @staticmethod
    def demo_mathematica_draw_bitcoin_price():
        mathematica.call_mathematica("..\\buffer\\export.m", {"bitcoinPrice": routine.get_bitcoin_price()}, "outX.png")

class QuandlOperations():
    quandlautth = "***" #TODO censored

    def __init__(self, ):
        print(self.quandlautth)
        self.cache = {}

    def get(self, key, **optional):
        # Zapackujeme UNIQUIE ID REQUESTU, teda KEY+optional
        optional["__dataset_id"] = key;
        unique_frozen_access = frozenset(optional)

        if self.cache.get(unique_frozen_access, None) is None:
            self.cache[unique_frozen_access] = Quandl.get(key, authtoken=self.quandlautth, **optional)

        return self.cache[unique_frozen_access]

class mathematica():
    @staticmethod
    def _call_kernel(script_name):
        return_code = subprocess.call("math.exe -script {}".format(script_name), shell=True)
        print(return_code)

    @staticmethod
    def _create_json_file(packed_dir):
        with open("..\\buffer\input.json", "w") as filehandle:
            filehandle.write(json.dumps(packed_dir))

    @staticmethod
    def call_mathematica(mathematica_script, packed_dir, output_file="out.png"):
        packed_dir.update({"META_OUTPUT_FILENAME": output_file})
        mathematica._create_json_file(packed_dir)
        mathematica._call_kernel(mathematica_script)

if __name__ == "__main__":
    single = QuandlOperations()
    routine.demo_mathematica_draw_bitcoin_price()


# print(get_bitcoin_price())


