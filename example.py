from grobid_client.grobid_client import GrobidClient


client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument","./resources/test",output="./resources/test_out/", consolidate_citations=True, tei_coordinates=True, force=True)


