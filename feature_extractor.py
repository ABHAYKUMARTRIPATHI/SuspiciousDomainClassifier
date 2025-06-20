import numpy as np
import pandas as pd
import re
import whois

def extract_features(domains):
    feature_list = []
    for domain in domains:
        length = len(domain)
        num_dots = domain.count('.')
        num_digits = sum(c.isdigit() for c in domain)
        entropy = -sum(p * np.log2(p) for p in [float(domain.count(c))/length for c in set(domain)])
        try:
            whois_info = whois.whois(domain)
            age = (pd.Timestamp.now() - pd.to_datetime(whois_info.creation_date)).days
        except:
            age = -1  # fallback in case of WHOIS failure
        feature_list.append([length, num_dots, num_digits, entropy, age])

    return pd.DataFrame(feature_list, columns=["length", "num_dots", "num_digits", "entropy", "domain_age"])
