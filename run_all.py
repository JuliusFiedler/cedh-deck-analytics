import subprocess
from s1_edh16_scrape import main as m1
from s2_moxfield_scrape import scrape_deck_pages
from s3_deck_preprocessing import preprocess_decklists
from s4_basic_decklist_analytics import analyze_card_usage
from s5_winrate_based_analytics import main as m5

#todo automatically run all
#todo auto setup requirements

scripts = [
    "1_edh16_scrape.py",
    "2_moxfield_scrape.py",
    "3_deck_preprocessing.py",
    "4_basic_decklist_analytics.py",
    "5_winrate_based_analytics.py"
]

if __name__ == "__main__":
    #todo: automatically initialize the scripts, so I don't need to type this out. Just look for scripts that are in the same directory
    # for script in scripts:
    #     subprocess.run(["python", script], check=True)
    m1()
    scrape_deck_pages()
    preprocess_decklists()
    analyze_card_usage()
    m5()


