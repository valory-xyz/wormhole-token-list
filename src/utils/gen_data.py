"""
motivation for this config being in python: json is easy to screw up

we'll maintain settings in dicts here and then generate json and markdown outputs
"""
import copy
import pandas as pd
import os


dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

TOKENS = {
  ##################
  # 1. Solana native
  ##################
  "SOL": {
    "symbol": "SOL",  # technically wrapped SOL
    "name": "SOL (Wormhole)",
    "destAddresses": {
      "eth": "0xD31a59c85aE9D8edEFeC411D448f90841571b89c",
      "terra": "terra190tqwgqx7s8qrknz6kckct7v607cu068gfujpk",
      "bsc": "0xfA54fF1a158B5189Ebba6ae130CEd6bbd3aEA76e",
      "avax": "0xFE6B19286885a4F7F55AdAD09C3Cd1f906D2478F",
    },
    "origin": "sol",
    "sourceAddress": "So11111111111111111111111111111111111111112",
    "coingeckoId": "solana",
  },
  "mSOL": {
    "symbol": "mSOL",
    "name": "Marinade staked SOL (Wormhole)",
    "destAddresses": {
      "eth": "0x756bFb452cFE36A5Bc82e4F5f4261A89a18c242b",
      "terra": "terra1qvlpf2v0zmru3gtex40sqq02wxp39x3cjh359y",
    },
    "origin": "sol",
    "sourceAddress": "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So",
    "coingeckoId": "marinade-staked-sol",
  },
  "USDCso": {
    "symbol": "USDCso",
    "name": "USD Coin (Wormhole from Solana)",
    "destAddresses": {
      "eth": "0x41f7B8b9b897276b7AAE926a9016935280b44E97",
      "terra": "terra1e6mq63y64zcxz8xyu5van4tgkhemj3r86yvgu4",
      "bsc": "0x91Ca579B0D47E5cfD5D0862c21D5659d39C8eCf0",
      "avax": "0x0950Fc1AD509358dAeaD5eB8020a3c7d8b43b9DA",
    },
    "origin": "sol",
    "sourceAddress": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    "coingeckoId": "usd-coin",
  },
  "USDTso": {
    "symbol": "USDTso",
    "name": "Tether USD (Wormhole from Solana)",
    "destAddresses": {
      "eth": "0x1CDD2EaB61112697626F7b4bB0e23Da4FeBF7B7C",
      "terra": "terra1hd9n65snaluvf7en0p4hqzse9eqecejz2k8rl5",
      "bsc": "0x49d5cC521F75e13fa8eb4E89E9D381352C897c96",
      "avax": "0xF0FF231e3F1A50F83136717f287ADAB862f89431",
    },
    "origin": "sol",
    "sourceAddress": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB",
    "coingeckoId": "tether",
  },
  "RAY": {
    "symbol": "RAY",
    "name": "Raydium (Wormhole)",
    "destAddresses": {
      "eth": "0xE617dd80c621a5072bD8cBa65E9d76c07327004d",
      "terra": "terra1ht5sepn28z999jx33sdduuxm9acthad507jg9q",
      "bsc": "0x13b6A55662f6591f8B8408Af1C73B017E32eEdB8",
    },
    "origin": "sol",
    "sourceAddress": "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R",
    "coingeckoId": "raydium",
  },
  "SBR": {
    "symbol": "SBR",
    "name": "Saber (Wormhole)",
    "destAddresses": {
      "terra": "terra17h82zsq6q8x5tsgm5ugcx4gytw3axguvzt4pkc",
      "bsc": "0x75344E5693ed5ecAdF4f292fFeb866c2cF8afCF1",
    },
    "origin": "sol",
    "sourceAddress": "0x75344E5693ed5ecAdF4f292fFeb866c2cF8afCF1",
    "coingeckoId": "saber",
  },
  "SRMso": {
    "symbol": "SRMso",
    "name": "Serum (Wormhole)",
    "destAddresses": {
      "eth": "0xE3ADAA4fb7c92AB833Ee08B3561D9c434aA2A3eE",
      "terra": "terra1dkam9wd5yvaswv4yq3n2aqd4wm5j8n82qc0c7c",
      "bsc": "0x12BeffdCEcb547640DC30e1495E4B9cdc21922b4",
    },
    "origin": "sol",
    "sourceAddress": "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt",
    "coingeckoId": "serum",
  },

  #####################
  # 2. Ethereum native
  #####################
  "ETH": {  # WETH
    "symbol": "ETH",
    "name": " (Wormhole)",
    "destAddresses": {
      "sol": "7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs",
      "bsc": "0x4DB5a66E937A9F4473fA95b1cAF1d1E1D62E29EA",
      "terra": "terra14tl83xcwqjy0ken9peu4pjjuu755lrry2uy25r",
      "matic": "0x11CD37bb86F65419713f30673A480EA33c826872",
      "avax": "0x8b82A291F83ca07Af22120ABa21632088fC92931",
    },
    "origin": "eth",
    "sourceAddress": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "coingeckoId": "ether",
  },
  "USDCet": {
    "symbol": "USDCet",
    "name": "USD Coin (Wormhole from Ethereum)",
    "destAddresses": {
      "sol": "A9mUU4qviSctJVPJdBJWkb28deg915LYJKrzQ19ji3FM",
      "terra": "terra1pepwcav40nvj3kh60qqgrk8k07ydmc00xyat06",
      "bsc": "0xB04906e95AB5D797aDA81508115611fee694c2b3",
      "avax": "0xB24CA28D4e2742907115fECda335b40dbda07a4C",
    },
    "origin": "eth",
    "sourceAddress": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "coingeckoId": "usd-coin",
  },
  "USDTet": {
    "symbol": "USDTet",
    "name": "Tether USD (Wormhole from Ethereum)",
    "destAddresses": {
      "sol": "Dn4noZ5jgGfkntzcQSUZ8czkreiZ1ForXYoV2H8Dm7S1",
      "terra": "terra1ce06wkrdm4vl6t0hvc0g86rsy27pu8yadg3dva",
      "bsc": "0x524bC91Dc82d6b90EF29F76A3ECAaBAffFD490Bc",
      "matic": "0x9417669fBF23357D2774e9D421307bd5eA1006d2",
    },
    "origin": "eth",
    "sourceAddress": "0xdac17f958d2ee523a2206206994597c13d831ec7",
    "coingeckoId": "tether",
  },
  "BUSDet": {
    "symbol": "BUSDet",
    "name": "Binance USD (Wormhole from Ethereum)",
    "destAddresses": {
      "sol": "33fsBLA8djQm82RpHmE3SuVrPGtZBWNYExsEUeKX1HXX",
      "bsc": "0x035de3679E692C471072d1A09bEb9298fBB2BD31",
    },
    "origin": "eth",
    "sourceAddress": "0x4fabb145d64652a948d72533023f6e7a623c7c53",
    "coingeckoId": "binance-usd",
  },
  "FRAX": {
    "symbol": "FRAX",
    "name": "Frax (Wormhole)",
    "destAddresses": {
      "sol": "FR87nWEUxVgerFGhZM8Y4AggKGLnaXswr1Pd8wZ4kZcp",
    },
    "origin": "eth",
    "sourceAddress": "0x853d955acef822db058eb8505911ed77f175b99e",
    "coingeckoId": "frax",
  },

  #################
  # 3. Terra native
  #################
  "UST": {
    "symbol": "UST",
    "name": "UST (Wormhole)",
    "destAddresses": {
      "eth": "0xa693b19d2931d498c5b318df961919bb4aee87a5",
      "bsc": "0x3d4350cD54aeF9f9b2C29435e0fa809957B3F30a",
      "matic": "0xE6469Ba6D2fD6130788E0eA9C0a0515900563b59",
      "avax": "0xb599c3590F42f8F995ECfa0f85D2980B76862fc1",
    },
    "origin": "terra",
    "sourceAddress": "uusd",
    "coingeckoId": "terra-usd",
  },
  "LUNA": {
    "symbol": "LUNA",
    "name": "LUNA (Wormhole)",
    "destAddresses": {
      "eth": "0xbd31ea8212119f94a611fa969881cba3ea06fa3d",
      "bsc": "0x156ab3346823B651294766e23e6Cf87254d68962",
      "matic": "0x9cd6746665D9557e1B9a775819625711d0693439",
      "avax": "0x70928E5B188def72817b7775F0BF6325968e563B",
    },
    "origin": "terra",
    "sourceAddress": "uluna",
    "coingeckoId": "terra-luna",
  },

  ###################
  # 4. Polygon native
  ###################
  "USDCpo": {
    "symbol": "USDCpo",  # double-bridged tether: ERC-20 -> Polygon (via PoS bridge)
    "name": "USD Coin (PoS) (Wormhole from Polygon)",
    "destAddresses": {
      "sol": "E2VmbootbVCBkMNNxKQgCLMS1X3NoGMaYAsufaAsf7M",
      "eth": "0x566957eF80F9fd5526CD2BEF8BE67035C0b81130",
      "terra": "terra1kkyyh7vganlpkj0gkc2rfmhy858ma4rtwywe3x",
      "bsc": "0x672147dD47674757C457eB155BAA382cc10705Dd",
      "avax": "0x543672E9CBEC728CBBa9C3Ccd99ed80aC3607FA8",
    },
    "origin": "matic",
    "sourceAddress": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    "coingeckoId": "usd-coin",
  },
  "MATICpo": {
    # this is mega-confusing because there is
    # 1. ERC-20 MATIC (we call MATICet)
    # 2. MATIC (native token of polygon) (0x0000000000000000000000000000000000001010)
    # 3. wrapped MATIC (we call MATICpo)
    "symbol": "MATICpo",
    "name": "MATIC (Wormhole from Polygon)",
    "destAddresses": {
      "sol": "Gz7VkD4MacbEB6yC5XD3HcumEiYx2EtDYYrfikGsvopG",  # covered by token-list
      "eth": "0x7c9f4C87d911613Fe9ca58b579f737911AAD2D43",
      "terra": "terra1dtqlfecglk47yplfrtwjzyagkgcqqngd5lgjp8",
      "bsc": "0xc836d8dC361E44DbE64c4862D55BA041F88Ddd39",
      "avax": "0xf2f13f0B7008ab2FA4A2418F4ccC3684E49D20Eb",
    },
    "origin": "matic",
    "sourceAddress": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
    "coingeckoId": "polygon",
  },

  #################
  # 5. AVAX native
  #################
  "AVAX": {
    "symbol": "AVAX",  # technically wrapped AVAX
    "name": "AVAX (Wormhole)",
    "destAddresses": {
      "sol": "KgV1GvrHQmRBY8sHQQeUKwTm2r2h8t4C8qt12Cw1HVE",  # covered by token-list
      "eth": "0x85f138bfEE4ef8e540890CFb48F620571d67Eda3",
      "terra": "terra1hj8de24c3yqvcsv9r8chr03fzwsak3hgd8gv3m",
      "bsc": "0x96412902aa9aFf61E13f085e70D3152C6ef2a817",
      "matic": "0x7Bb11E7f8b10E9e571E5d8Eace04735fDFB2358a",
    },
    "origin": "avax",
    "sourceAddress": "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7",
    "coingeckoId": "avalanche",
  },
  "JOE": {
    "symbol": "JOE",
    "name": "JoeToken (Wormhole)",
    "destAddresses": {
      "sol": "CriXdFS9iRAYbGEQiTcUqbWwG9RBmYt5B6LwTnoJ61Sm",  # covered by token-list
    },
    "origin": "avax",
    "sourceAddress": "0x6e84a6216ea6dacc71ee8e6b0a5b7322eebc0fdd",
    "coingeckoId": "joe",
  },
  #################
  # 6. Oasis native
  #################
  # "": {
  #   "symbol": "",
  #   "name": " (Wormhole)",
  #   "destAddresses": {
  #     "eth": "",
  #     "bsc": "",
  #     "terra": "",
  #   },
  #   "origin": "",
  #   "sourceAddress": "",
  #   "coingeckoId": "",
  # },
}

SOURCE_INFO = {
  'eth': ('Ethereum', 'et', "https://etherscan.io", "https://etherscan.io/address/0x3ee18B2214AFF97000D974cf647E7C347E8fa585"),
  'bsc': ('BSC', 'bs', "https://bscscan.com", "https://bscscan.com/address/0xB6F6D86a8f9879A9c87f643768d9efc38c1Da6E7"),
  'terra': ('Terra', 'te', "https://finder.terra.money/columbus-5", "https://finder.terra.money/columbus-5/address/terra10nmmwe8r3g99a9newtqa7a75xfgs2e8z87r2sf"),
  'matic': ('Polygon', 'po', "https://polygonscan.com", "https://polygonscan.com/address/0x5a58505a96d1dbf8df91cb21b54419fc36e93fde"),
  'avax': ('Avalanche', 'av', "https://snowtrace.io", "https://snowtrace.io/address/0x0e082f06ff657d94310cb8ce8b0d9a04541d8052"),
  'sol': ('Solana', 'so', "https://solscan.io", "https://solscan.io/account/wormDTUJ6AWPNvk59vGQbDvGJmqbDTdgWgAqcLBCgUb"),
  # 'algo': ('Algorand', 'al'),
}


def _link_address(dest, addr):
  category = 'address' if dest == 'terra' else 'token'
  return "[%s](%s/%s/%s)" % (addr, SOURCE_INFO[dest][2], category, addr)


def _link_coingecko(name, coingecko_id):
  if pd.isna(coingecko_id):
    return name
  else:
    return "[%s](http://coingecko.com/en/coins/%s)" % (name, coingecko_id)


def _link_source_address(source_chain, source_addr):
  source_contract = "%s/address/%s" % (SOURCE_INFO[source_chain][2] , source_addr)
  return "[%s](%s)" % (source_addr, source_contract)


def gen_markdown(dest):
  dest_full = SOURCE_INFO[dest][0]
  tokens = {}
  for coin, entry in TOKENS.items():
    if dest not in entry['destAddresses']:
      continue
    entry = copy.deepcopy(entry)
    entry['address'] = entry['destAddresses'][dest]
    entry.pop('destAddresses')
    tokens[coin] = entry
  df = pd.DataFrame(tokens.values())
  if df.shape[0] == 0:
    print('no tokens for dest=%s' % dest)
    return
  df = df.sort_values(by='symbol')
  df['name'] = [_link_coingecko(n, c) for (n, c) in zip(df['name'].values, df['coingeckoId'].values)]
  df['address'] = [_link_address(dest, x) for x in df['address'].values]
  df['sourceAddress'] = [_link_source_address(x, y) for (x,y) in
                         zip(df['origin'].values, df['sourceAddress'].values)]
  df['origin'] = [SOURCE_INFO[x][0].lower() for x in df['origin'].values]
  df['symbol_reprise'] = df['symbol']

  df = df.drop(['coingeckoId'], axis=1)

  df = df[['symbol', 'name', 'address', 'origin', 'sourceAddress', 'symbol_reprise']]

  # col_rename = {
  # }
  # df.columns = [col_rename.get(x, x) for x in df.columns]

  txt = df.to_markdown(index=False).replace('symbol_reprise', 'symbol')
  header = """
Known tokens (wormholed to %s)
===================================
  """ % dest_full
  outpath = os.path.join(dir_path, 'dest_%s.md' % dest_full.lower())
  with open(outpath, 'w') as f:
    f.write(header + '\n' + txt)
  print('wrote %s' % outpath)


if __name__ == "__main__":
  for dest in ['eth', 'bsc', 'terra', 'avax', 'matic']:
    gen_markdown(dest)
