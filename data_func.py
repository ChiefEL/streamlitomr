import os
from huggingface_hub import Repository
import pandas as pd

DATASET_REPO_URL = "https://huggingface.co/datasets/mertbozkurt/school_data"
DATA_FILENAME = "untitled.csv"
DATA_FILE = os.path.join("data", DATA_FILENAME)
HF_TOKEN = "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"

def pull_read():
    
    repo = Repository(
        local_dir="data", clone_from=DATASET_REPO_URL, use_auth_token=HF_TOKEN
        )
    
    with open(DATA_FILE) as csvfile:
        df = pd.read_csv(csvfile) 
        df = pd.DataFrame(df)
    
    return repo, df

def make_new_data(sinif_kodu,ogrenci_no,ders_kodu,notu,yanlislar):
    yeni_satir = {"sinif_kodu": sinif_kodu, 
              "ogrenci_no": ogrenci_no, 
              "ders_kodu": ders_kodu,
              "notu": notu, 
             "yanlis_sorulari": yanlislar}
    new_data = pd.DataFrame([yeni_satir])
    return new_data 
    
def update(new_data, ex_df):
    updated_df = pd.concat([ex_df, new_data])
    return updated_df
    
def save_and_push(dataFrame,repo):
    dataFrame.to_csv("C:/Users/Admin/Desktop/CVfinal/optical-mark-recognition-main/data/untitled.csv",index=False)
    commit_url = repo.push_to_hub()
    return commit_url

"""repo, repo_df = pull_read()
new_data = make_new_data(12,151718,56,80,"2,3,5")
updated_df = update(new_data,repo_df)
save_and_push(updated_df,repo)"""