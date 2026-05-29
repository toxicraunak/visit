#CREDIT CHANGE KI TO SAMAJH LENA🌚 GRILS CREDIT CHANGE KAR SAKTI HAI KYUKI WO GRILS(PAPA KI PARI HAI) MAJAK ME LIKHA KOI DIL PE MAT LENA AHHAHAHAHAHAHAHAAH

from flask import Flask, jsonify, request
import aiohttp
import asyncio
import json
import threading
import time
import os
import glob
import sys
import warnings
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append("/")

from byte import encrypt_api, Encrypt_ID
from visit_count_pb2 import Info
from protobuf import my_pb2, output_pb2

app = Flask(__name__)

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

RIzeR_GaY = {}
GaY = 69 #JITNE ACCOUNT HONGE UTNA HI RAKHNA HAHAHAHAHA JAYADA MAT KARNA LIKE 200 ACCOUNT HAI TO 200
GaY_ReFrEsH = 2 * 60 * 60
LaSt_GaY = 0
ErEN_gAY = ThreadPoolExecutor(max_workers=100)

AES_KEY = b'Yg&tc%DEuh6%Zc^8'
AES_IV = b'6oyZDr22E3ychjM%'

def UNkNOwn_Gay(password, uid):
    url = "https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant"
    headers = {
        "User-Agent": "GarenaMSDK/4.0.19P4(G011A ;Android 9;en;US;)",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    try:
        r = requests.post(url, headers=headers, data=data, timeout=10)
        j = r.json()
        token = (j.get("access_token") or j.get("token") or j.get("session_key") or j.get("jwt") or (j.get("data") or {}).get("token"))
        return {"access_token": token, "open_id": j.get("open_id"), "uid": j.get("uid"), "raw": j}
    except Exception as e:
        return {"error": f"OAuth failed: {str(e)}"}

def YoUr_MoM(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(plaintext, AES.block_size)
    return cipher.encrypt(padded_message)

def ChU_tiYa(response_content):
    try:
        example_msg = output_pb2.Garena_420()
        example_msg.ParseFromString(response_content)
        response_dict = {}
        lines = str(example_msg).split("\n")
        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                response_dict[key.strip()] = value.strip().strip('"')
        return response_dict
    except Exception as e:
        return {"error": str(e)}

def ReSPeCt_GiRLs(uid, password):
    oauth_data = UNkNOwn_Gay(password, uid)
    if "error" in oauth_data or not oauth_data.get("access_token"):
        return {"success": False, "error": oauth_data.get("error", "No access token"), "uid": uid}
    access_token = oauth_data["access_token"]
    open_id = oauth_data.get("open_id", "")
    game_data = my_pb2.GameData()
    game_data.timestamp = "2024-12-05 18:15:32"
    game_data.game_name = "free fire"
    game_data.game_version = 1
    game_data.version_code = "1.108.3"
    game_data.os_info = "Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)"
    game_data.device_type = "Handheld"
    game_data.network_provider = "Verizon Wireless"
    game_data.connection_type = "WIFI"
    game_data.screen_width = 1280
    game_data.screen_height = 960
    game_data.dpi = "240"
    game_data.cpu_info = "ARMv7 VFPv3 NEON VMH | 2400 | 4"
    game_data.total_ram = 5951
    game_data.gpu_name = "Adreno (TM) 640"
    game_data.gpu_version = "OpenGL ES 3.0"
    game_data.user_id = "Google|74b585a9-0268-4ad3-8f36-ef41d2e53610"
    game_data.ip_address = "172.190.111.97"
    game_data.language = "en"
    game_data.open_id = open_id
    game_data.access_token = access_token
    game_data.platform_type = 4
    game_data.device_form_factor = "Handheld"
    game_data.device_model = "Asus ASUS_I005DA"
    game_data.field_60 = 32968
    game_data.field_61 = 29815
    game_data.field_62 = 2479
    game_data.field_63 = 914
    game_data.field_64 = 31213
    game_data.field_65 = 32968
    game_data.field_66 = 31213
    game_data.field_67 = 32968
    game_data.field_70 = 4
    game_data.field_73 = 2
    game_data.library_path = "/data/app/com.dts.freefireth-QPvBnTUhYWE-7DMZSOGdmA==/lib/arm"
    game_data.field_76 = 1
    game_data.apk_info = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-QPvBnTUhYWE-7DMZSOGdmA==/base.apk"
    game_data.field_78 = 6
    game_data.field_79 = 1
    game_data.os_architecture = "32"
    game_data.build_number = "2019117877"
    game_data.field_85 = 1
    game_data.graphics_backend = "OpenGLES2"
    game_data.max_texture_units = 16383
    game_data.rendering_api = 4
    game_data.encoded_field_89 = "\u0017T\u0011\u0017\u0002\b\u000eUMQ\bEZ\u0003@ZK;Z\u0002\u000eV\ri[QVi\u0003\ro\t\u0007e"
    game_data.field_92 = 9204
    game_data.marketplace = "3rd_party"
    game_data.encryption_key = "KqsHT2B4It60T/65PGR5PXwFxQkVjGNi+IMCK3CFBCBfrNpSUA1dZnjaT3HcYchlIFFL1ZJOg0cnulKCPGD3C3h1eFQ="
    game_data.total_storage = 111107
    game_data.field_97 = 1
    game_data.field_98 = 1
    game_data.field_99 = "4"
    game_data.field_100 = "4"
    serialized_data = game_data.SerializeToString()
    encrypted_data = YoUr_MoM(AES_KEY, AES_IV, serialized_data)
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/octet-stream",
        'Expect': "100-continue",
        'X-GA': "v1 1",
        'X-Unity-Version': "2018.4.11f1",
        'ReleaseVersion': "OB53"
    }
    try:
        response = requests.post(url, data=encrypted_data, headers=headers, verify=False, timeout=15)
        if response.status_code == 200:
            parsed = ChU_tiYa(response.content)
            jwt_token = parsed.get("token", "")
            region = parsed.get("region", "BD")
            api_endpoint = parsed.get("api", "")
            status = parsed.get("status", "unknown")
            if jwt_token and jwt_token not in ["", "N/A", "null"]:
                return {"success": True, "uid": str(uid), "token": jwt_token, "region": region, "api": api_endpoint, "status": status}
            else:
                return {"success": False, "error": "No valid JWT", "uid": uid}
        else:
            return {"success": False, "error": f"HTTP {response.status_code}", "uid": uid}
    except Exception as e:
        return {"success": False, "error": str(e), "uid": uid}

def XoXo():
    try:
        all_accounts = []
        json_files = glob.glob("accounts-*.json")
        if not json_files:
            print(f"⚠️ No accounts files")
            return []
        for file_path in json_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        accounts_list = data
                    elif isinstance(data, dict):
                        accounts_list = [data]
                    else:
                        continue
                    for account in accounts_list:
                        if 'uid' in account and 'password' in account:
                            all_accounts.append({
                                "uid": str(account["uid"]),
                                "password": str(account["password"]),
                                "region": str(account.get("region", "BD")),
                                "name": account.get("name", ""),
                                "account_id": account.get("account_id", "N/A")
                            })
                print(f"✅ Loaded from {file_path}")
            except Exception as e:
                print(f"❌ Error loading {file_path}: {e}")
        print(f"✅ Total {len(all_accounts)} accounts")
        return all_accounts
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def DoNt_ChAnGe():
    global LaSt_GaY
    accounts = XoXo()
    if not accounts:
        return
    total_accounts = len(accounts)
    print(f"🔄 Generating JWT for {total_accounts} accounts in PARALLEL...")
    all_tokens_data = {}
    total_success = 0
    total_failed = 0
    future_to_account = {ErEN_gAY.submit(ReSPeCt_GiRLs, acc["uid"], acc["password"]): acc for acc in accounts}
    completed = 0
    for future in as_completed(future_to_account):
        account = future_to_account[future]
        completed += 1
        try:
            result = future.result()
            if completed % 10 == 0 or completed == total_accounts:
                print(f"⏳ Progress: {completed}/{total_accounts}")
            if result.get("success"):
                region = result["region"]
                if region not in all_tokens_data:
                    all_tokens_data[region] = []
                all_tokens_data[region].append({"uid": result["uid"], "token": result["token"], "region": region, "api": result.get("api", "")})
                total_success += 1
                print(f"✅ [{completed}] JWT for {result['uid']} ({region})")
            else:
                total_failed += 1
                print(f"❌ [{completed}] Failed for {account['uid']}: {result.get('error')}")
        except Exception as e:
            total_failed += 1
            print(f"❌ [{completed}] Exception: {e}")
    print(f"\n📊 Summary: ✅ {total_success} | ❌ {total_failed} | 📈 {(total_success/total_accounts*100):.1f}%")
    for region, tokens in all_tokens_data.items():
        token_file = BlAcK_Red(region)
        try:
            with open(token_file, "w") as f:
                json.dump(tokens, f, indent=2)
            print(f"💾 Saved {len(tokens)} tokens to {token_file}")
            if region in RIzeR_GaY:
                RIzeR_GaY[region]['all_tokens'] = [t["token"] for t in tokens]
                RIzeR_GaY[region]['total_tokens'] = len(tokens)
            else:
                RIzeR_GaY[region] = {'all_tokens': [t["token"] for t in tokens], 'current_index': 0, 'total_tokens': len(tokens)}
        except Exception as e:
            print(f"❌ Error: {e}")
    LaSt_GaY = time.time()
    print("✅ Completed!")

async def SiLeNt_KiLL():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, DoNt_ChAnGe)

def GaY_LoOp():
    while True:
        try:
            now = time.time()
            if now - LaSt_GaY >= GaY_ReFrEsH:
                DoNt_ChAnGe()
            time.sleep(60)
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)

def BlAcK_Red(server_name):
    if server_name == "IND":
        return "token_ind.json"
    elif server_name in {"BR", "US", "SAC", "NA"}:
        return "token_br.json"
    elif server_name == "VN":
        return "token_vn.json"
    else:
        return "token_bd.json"

def UNknown(server_name):
    try:
        path = BlAcK_Red(server_name)
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            data = json.load(f)
        tokens = [item["token"] for item in data if "token" in item and item["token"] not in ["", "N/A"]]
        return tokens
    except Exception as e:
        app.logger.error(f"❌ Error: {e}")
        return []

def ReSPeCt_Me(server_name):
    global RIzeR_GaY
    if server_name not in RIzeR_GaY:
        all_tokens = UNknown(server_name)
        RIzeR_GaY[server_name] = {'all_tokens': all_tokens, 'current_index': 0, 'total_tokens': len(all_tokens)}
    rotation_data = RIzeR_GaY[server_name]
    all_tokens = rotation_data['all_tokens']
    current_index = rotation_data['current_index']
    total_tokens = rotation_data['total_tokens']
    if total_tokens == 0:
        return []
    start_index = current_index
    end_index = (current_index + GaY) % total_tokens
    if start_index < end_index:
        tokens_for_request = all_tokens[start_index:end_index]
    else:
        tokens_for_request = all_tokens[start_index:] + all_tokens[:end_index]
    RIzeR_GaY[server_name]['current_index'] = end_index
    print(f"🔑 Token rotation: Using {start_index+1}-{end_index if end_index > start_index else total_tokens} (Total: {total_tokens})")
    return tokens_for_request

def YoUr_BaP(server_name):
    if server_name == "IND":
        return "https://client.ind.freefiremobile.com/GetPlayerPersonalShow"
    elif server_name in {"BR", "US", "SAC", "NA"}:
        return "https://client.us.freefiremobile.com/GetPlayerPersonalShow"
    elif server_name == "VN":
        return "https://clientbp.ggwhitehawk.com/GetPlayerPersonalShow"
    else:
        return "https://clientbp.ggblueshark.com/GetPlayerPersonalShow"

def No_NAMe(response_data):
    try:
        info = Info()
        info.ParseFromString(response_data)
        player_data = {
            "uid": info.AccountInfo.UID if info.AccountInfo.UID else 0,
            "nickname": info.AccountInfo.PlayerNickname if info.AccountInfo.PlayerNickname else "",
            "likes": info.AccountInfo.Likes if info.AccountInfo.Likes else 0,
            "region": info.AccountInfo.PlayerRegion if info.AccountInfo.PlayerRegion else "",
            "level": info.AccountInfo.Levels if info.AccountInfo.Levels else 0
        }
        return player_data
    except Exception as e:
        app.logger.error(f"❌ Error: {e}")
        return None

async def LoVe_HaTe(session, url, token, uid, data):
    headers = {"ReleaseVersion": "OB53", "X-GA": "v1 1", "Authorization": f"Bearer {token}", "Host": url.replace("https://", "").split("/")[0]}
    try:
        async with session.post(url, headers=headers, data=data, ssl=False) as resp:
            if resp.status == 200:
                response_data = await resp.read()
                return True, response_data
            else:
                return False, None
    except Exception as e:
        return False, None

async def TiMe_TRaVeL(tokens, uid, server_name, target_success=10000):
    url = YoUr_BaP(server_name)
    connector = aiohttp.TCPConnector(limit=0)
    total_success = 0
    total_sent = 0
    first_success_response = None
    player_info = None
    async with aiohttp.ClientSession(connector=connector) as session:
        encrypted = encrypt_api("08" + Encrypt_ID(str(uid)) + "1801")
        data = bytes.fromhex(encrypted)
        while total_success < target_success:
            remaining = target_success - total_success
            batch_size = min(remaining, len(tokens))
            if batch_size == 0:
                break
            tasks = []
            for i in range(batch_size):
                token_index = i % len(tokens)
                tasks.append(asyncio.create_task(LoVe_HaTe(session, url, tokens[token_index], uid, data)))
            results = await asyncio.gather(*tasks)
            if first_success_response is None:
                for success, response in results:
                    if success and response is not None:
                        first_success_response = response
                        player_info = No_NAMe(response)
                        break
            batch_success = sum(1 for r, _ in results if r)
            total_success += batch_success
            total_sent += batch_size
            print(f"🔑 Using {len(tokens)} tokens | Visits sent: {batch_size}, Success: {batch_success}, Total: {total_success}/{target_success}")
            if batch_success == 0:
                await asyncio.sleep(0.1)
    return total_success, total_sent, player_info

@app.route('/visit', methods=['GET'])
def CrAzY_BoY():
    region = request.args.get('region', '').upper()
    uid = request.args.get('uid', '')
    if not region or not uid:
        return jsonify({"error": "Missing region and uid"}), 400
    try:
        uid = int(uid)
    except ValueError:
        return jsonify({"error": "UID must be number"}), 400
    tokens = ReSPeCt_Me(region)
    target_success = 10000
    if not tokens:
        return jsonify({"error": "No valid tokens"}), 500
    print(f"🚀 Sending to UID: {uid} in region: {region}")
    total_success, total_sent, player_info = asyncio.run(TiMe_TRaVeL(tokens, uid, region, target_success=target_success))
    if player_info:
        return jsonify({
            "fail": target_success - total_success,
            "level": player_info.get("level", 0),
            "likes": player_info.get("likes", 0),
            "nickname": player_info.get("nickname", ""),
            "region": player_info.get("region", ""),
            "success": total_success,
            "uid": player_info.get("uid", 0),
            "tokens_used": len(tokens),
             "credit": "⭐Papa Is Code Ka Papa @vaibhavff570"
        }), 200
    else:
        return jsonify({"error": "Could not decode"}), 500

@app.route('/token-status/<string:server>', methods=['GET'])
def GaY_StAtUs(server):
    server = server.upper()
    if server in RIzeR_GaY:
        rotation_data = RIzeR_GaY[server]
        return jsonify({
            "server": server,
            "total_tokens": rotation_data['total_tokens'],
            "current_index": rotation_data['current_index'],
            "tokens_per_request": GaY,
            "method": "ReSPeCt_GiRLs"
        })
    else:
        return jsonify({"error": "No tokens"}), 404

@app.route('/refresh-tokens', methods=['POST'])
def XxX():
    asyncio.run(SiLeNt_KiLL())
    return jsonify({"status": "refresh_started", "method": "ReSPeCt_GiRLs"}), 200

@app.route('/accounts-status', methods=['GET'])
def BaP_StAtUs():
    accounts = XoXo()
    status = {"accounts_loaded": len(accounts), "last_refresh": LaSt_GaY, "method": "ReSPeCt_GiRLs"}
    for region in ["IND", "BD", "BR", "VN"]:
        path = BlAcK_Red(region)
        status[region] = {"exists": os.path.exists(path), "size": os.path.getsize(path) if os.path.exists(path) else 0}
    return jsonify(status)

@app.route('/test-jwt', methods=['GET'])
def ErEN_gAY_TeSt():
    uid = request.args.get('uid')
    password = request.args.get('password')
    if not uid or not password:
        return jsonify({"error": "Missing uid and password"}), 400
    result = ReSPeCt_GiRLs(uid, password)
    return jsonify(result)

if __name__ == "__main__":
    print("🚀 Starting with ReSPeCt_GiRLs method")
    asyncio.run(SiLeNt_KiLL())
    refresh_thread = threading.Thread(target=GaY_LoOp, daemon=True)
    refresh_thread.start()
    print("✅ Background started")
    port = int(os.environ.get("PORT", 5070))
    app.run(host="0.0.0.0", port=port, debug=False)