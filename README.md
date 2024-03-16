# TrVD: Deep Semantic Extraction via AST Decomposition for Vulnerability Detection
The explosive growth of software vulnerabilities poses a serious threat to the system security and has become one of the urgent problems of the day. Yet, existing vulnerability detection methods show limitations in reaching the balance between the detection accuracy, efficiency and applicability. To this end, this paper proposes TrVD (abstract syntax Tree decomposition based Vulnerability Detector), which exposes the indicative semantics implied deeply in the source code fragments for accurate and efficient vulnerability detection following a divide-and-conquer strategy. To ease the capture of subtle semantic features, TrVD converts the AST
of a code fragment into ordered sub-trees of restricted sizes and depths with a novel decomposition algorithm. The semantics of each sub-tree can thus be effectively collected with a carefully designed tree-structured neural network. Finally, a Transformer-style encoder is utilized to summarize them up into a dense vector, with learning additional long-range semantics relationships among the sub-trees and distilling the semantics that are more informative to pin down the vulnerable patterns.

## Design of TrVD
![image](https://github.com/XUPT-SSS/TrVD/assets/118888372/2f02f149-6674-41d4-b727-75990972899a)


## Dataset
We collect a dataset from Software Assurance Reference Dataset (SARD) ( https://samate.nist.gov/SRD/index.php) which is a project maintained by National Institute of Standards and Technology (NIST) (https://www.nist.gov/). SARD contains a large number of production, synthetic, and academic security flaws or vulnerabilities (i.e., bad functions) and many good functions. In our paper, we focus on detecting vulnerability in C/C++, therefore, we only select functions written in C/C++ in SARD. Data obtained from SARD consists of 98,181 vulnerable functions and 166,641 non-vulnerable functions.

## Source

### Step 0: Install the required packages
```bash
pip install -r requirements.txt
```

### Step 0.1: Prepare the dataset
```bash
unzip ./dataset/dataset.zip -d ./
python3 ./partition_data.py
```

### Step1:Code normalization
Normalize the code with normalization.py
```
python ./normalization.py
```

### step2: AST decomposition 
```
python ./pipeline.py
```

### Step3: Train TrVD vulnerability detector
```
python ./train.py
```

### Step4: Evaluate our model
```
python ./evaluation.py
```
