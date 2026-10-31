import akshare as ak
import pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parent
print(ak.__version__)
help(ak.stock_zh_a_hist)#请求帮助
# df = ak.stock_zh_a_hist(
#     symbol="600519",
#     period="daily",
#     start_date="20241201",
#     end_date="20241210",
#     adjust="qfq")
df = ak.stock_zh_a_hist_tx(
    symbol="sh600519",
    start_date="20241201",
    end_date="20241210",
    adjust="qfq",
)
print(df.head())
print(df.shape)
print(df.columns)

out_dir = ROOT / "data" / "raw"
out_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(out_dir / "600519_daily.csv", index=False, encoding="utf-8-sig")
print("saved:", out_dir / "600519_daily.csv")
# (df.columns)
