import pybase64
import base64
import requests
import binascii
import os

# Define a fixed timeout for HTTP requests
TIMEOUT = 20  # seconds

# Define the fixed text for the initial configuration
fixed_text = """#profile-title: base64:8J+GkyBHaXRodWIgfCBCYXJyeS1mYXIg8J+ltw==
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/coldwater-10/V2ray-Configs
#profile-web-page-url: https://github.com/coldwater-10/V2ray-Configs
"""

# Base64 decoding function
def decode_base64(encoded):
    decoded = ""
    for encoding in ["utf-8", "iso-8859-1"]:
        try:
            decoded = pybase64.b64decode(encoded + b"=" * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded

# Function to decode base64-encoded links with a timeout
def decode_links(links):
    decoded_data = []
    for link in links:
        try:
            response = requests.get(link, timeout=TIMEOUT)
            encoded_bytes = response.content
            decoded_text = decode_base64(encoded_bytes)
            decoded_data.append(decoded_text)
        except requests.RequestException:
            pass  # If the request fails or times out, skip it
    return decoded_data

# Function to decode directory links with a timeout
def decode_dir_links(dir_links):
    decoded_dir_links = []
    for link in dir_links:
        try:
            response = requests.get(link, timeout=TIMEOUT)
            decoded_text = response.text
            decoded_dir_links.append(decoded_text)
        except requests.RequestException:
            pass  # If the request fails or times out, skip it
    return decoded_dir_links

# Filter function to select lines based on specified protocols
def filter_for_protocols(data, protocols):
    filtered_data = []
    for line in data:
        if any(protocol in line for protocol in protocols):
            filtered_data.append(line)
    return filtered_data

# Create necessary directories if they don't exist
def ensure_directories_exist():
    output_folder = os.path.abspath(os.path.join(os.getcwd(), ".."))
    base64_folder = os.path.join(output_folder, "Base64")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(base64_folder):
        os.makedirs(base64_folder)

    return output_folder, base64_folder

# Main function to process links and write output files
def main():
    output_folder, base64_folder = ensure_directories_exist()  # Ensure directories are created

    protocols = ["vmess", "vless", "trojan", "ss", "ssr", "hy2", "tuic", "warp://"]
    links = [
        "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/mix_base64",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/hysteria",
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/tuic",
        "https://raw.githubusercontent.com/freefq/free/master/v2",
        "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub",
        "https://raw.githubusercontent.com/AzadNetCH/Clash/main/V2Ray.txt",
        "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/v2",
        "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/vless",
        "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/ss",
        "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/ssr",
        "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/tr",
        "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/all2",
        "https://raw.githubusercontent.com/free18/v2ray/main/v2ray.txt",
        "https://raw.githubusercontent.com/allenfengjr/VlessSub/main/sub",
        "https://bitbucket.org/huwo1/proxy_nodes/raw/b90856fe7cb9c666223f3ad41c87d0e60c711590/proxy.md",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/sub",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/vless",
        "https://raw.githubusercontent.com/resasanian/Mirza/main/best",
        "https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt",
        "https://raw.githubusercontent.com/xiyaowong/freeFQ/main/v2ray",
        "https://raw.githubusercontent.com/iwxf/free-v2ray/master/index.html",
        "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/vmess",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/reality",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/temporary",
        "https://raw.githubusercontent.com/RescueNet/TelegramFreeServer/main/base64/checked",
        "https://raw.githubusercontent.com/vpei/Free-Node-Merge/main/o/node.txt",
        "https://raw.githubusercontent.com/Jsnzkpg/Jsnzkpg/Jsnzkpg/Jsnzkpg",
        "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
        "https://raw.githubusercontent.com/ssrsub/ssr/master/V2Ray",
        "https://raw.githubusercontent.com/ssrsub/ssr/master/ss-sub",
        "https://raw.githubusercontent.com/ssrsub/ssr/master/trojan",
        "https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray",
        "https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription_num",
        "https://freevpn878.hamidimorteza680.workers.dev/sub",
        "http://104.168.107.230/aggregate.txt",
        "https://sub.pmsub.me/base64",
        "https://gitea.com/proxypools/sub/raw/branch/main/ss/ss.txt",
        "https://gitea.com/proxypools/sub/raw/branch/main/ssr/ssr.txt",
        "https://gitea.com/proxypools/sub/raw/branch/main/vmess/vs.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/SS-Kcptun/ssconfig.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/ssconfig.txt",
        "https://raw.githubusercontent.com/Alvin9999/pac2/master/SSR/ssconfig.txt",
        "https://raw.githubusercontent.com/dingyu0321/linshi/main/ceshi",
        "https://raw.githubusercontent.com/junwei380/jcjd028/main/0928",
        "https://raw.githubusercontent.com/jsnjsnwbtwbt/2D2F/main/2C2F",
        "https://raw.githubusercontent.com/jsnjsnwbtwbt/TEzNC1jOTY1ZGE5OWM1ZT/main/Stable",
        "https://raw.githubusercontent.com/voken100g/AutoSSR/master/online",
        "https://raw.githubusercontent.com/voken100g/AutoSSR/master/recent",
        "https://muma16fx.netlify.app",
        "https://qiaomenzhuanfx.netlify.app",
        "https://raw.githubusercontent.com/Surfboardv2ray/Subs/main/Raw",
        "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/hy2",
        "https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/main/sub64",
        "https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/master/Eternity",
        "https://raw.githubusercontent.com/shirkerboy/scp/main/sub",
        "https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/Shenzo.txt",
        "https://raw.githubusercontent.com/MrPooyaX/SansorchiFucker/main/data.txt",
        "https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt",
        "https://raw.githubusercontent.com/mlabalabala/v2ray-node/main/vm_static_node.txt",
        "https://raw.githubusercontent.com/learnhard-cn/free_proxy_ss/main/free",
        "https://raw.githubusercontent.com/learnhard-cn/free_proxy_ss/main/v2ray/v2raysub",
        "https://raw.githubusercontent.com/lflflf999/0516/main/BX-JD",
        "https://raw.githubusercontent.com/Mr8AHAL/v2ray/main/SERVER.txt",
        "https://raw.githubusercontent.com/ripaojiedian/freenode/main/sub",
        "https://raw.githubusercontent.com/Lewis-1217/FreeNodes/main/bpjzx1",
        "https://raw.githubusercontent.com/Lewis-1217/FreeNodes/main/bpjzx2",
        "https://raw.githubusercontent.com/renyige1314/CLASH/main/CLASH",
        "https://raw.githubusercontent.com/hkaa0/permalink/main/proxy/V2ray",
        "https://raw.githubusercontent.com/sun9426/sun9426.github.io/main/subscribe/v2ray.txt",
        "https://bamarambash.monster/subscriptions/b8767a6a-1c30-11ee-ba76-9ee097a90b8b",
        "https://raw.githubusercontent.com/ts-sf/fly/main/v2",
        "https://raw.githubusercontent.com/mheidari98/.proxy/main/all",
        "https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Config_64base",
        "https://raw.githubusercontent.com/fanqiangfeee/freefq/main/v2ray",
        "https://raw.githubusercontent.com/Vauth/node/main/Main",
        "https://raw.githubusercontent.com/Vauth/node/main/Pro",
        "https://raw.githubusercontent.com/ZywChannel/free/main/sub",
        "https://raw.githubusercontent.com/Restia-Ashbell/cf_vless_sub/main/sub",
        "https://raw.githubusercontent.com/zengfr/free-vpn-subscribe/main/vpn_sub_.txt",
        "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUB/main/BASE64.txt",
        "https://freefq.neocities.org/free.txt",
    ]
    dir_links = [
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollector/main/vless_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollector/main/vmess_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollector/main/trojan_iran.txt",
        "https://raw.githubusercontent.com/coldwater-10/V2rayCollector/main/ss_iran.txt",
        "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt",
        "https://raw.githubusercontent.com/xc0000e9/deatnote/main/Hiddify-next.fragment",
        "https://raw.githubusercontent.com/m3hdio1/v2ray_sub/main/v2ray_sub.txt",
        "https://raw.githubusercontent.com/freev2rayconfig/V2RAY_SUB/main/v2ray.txt",
        "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/all2",
        "https://raw.githubusercontent.com/1Shervin/Sub/main/v2ray'
        "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/splitted/mixed'
        "https://panel.quickservice.sbs/gWQfDehzDHyfmKXWUK9N4sSL6fRn/2d0c6203-f715-4b14-973a-ac25e560b03e/all.txt?name=panel.quickservice.sbs-unknown&asn=unknown&mode=new'
        "https://confighub.site/sub.txt",
        "https://raw.githubusercontent.com/ImMyron/V2ray/main/Web",
        "https://raw.githubusercontent.com/ImMyron/V2ray/main/Telegram",
        "https://raw.githubusercontent.com/sarinaesmailzadeh/V2Hub/main/merged",
        "https://zebelkhan10.fallahpour25.workers.dev/sub/74f829f3-480b-4e7f-8039-9418d055375b",
        "https://raw.githubusercontent.com/mksshare/mksshare.github.io/main/README.md",
        "https://raw.githubusercontent.com/abshare/abshare.github.io/main/README.md",
        "https://raw.githubusercontent.com/tolinkshare/freenode/main/README.md",
        "https://raw.githubusercontent.com/mianfeifq/share/main/README.md",
        "https://raw.githubusercontent.com/imohammadkhalili/V2RAY/main/Mkhalili",
        "https://alienvpn402.github.io/AlienVPN402-subscribe-servers/",
        "https://alienvpn402.github.io/AlienVPN402-subscribe-servers-sing-box/",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/ss.txt",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/ssr.txt",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/trojan.txt",
        "https://raw.githubusercontent.com/skywolf627/ProxiesActions/main/subscribe/vmess.txt",
        "https://raw.githubusercontent.com/a2470982985/getNode/main/v2ray.txt",
        "https://raw.githubusercontent.com/mlabalabala/v2ray-node/main/nodefree_nodes_mod.txt",
        "https://raw.githubusercontent.com/mlabalabala/v2ray-node/main/nodefree_nodes_ori.txt",
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/config",
        "https://raw.githubusercontent.com/IranianCypherpunks/sub/main/newconfig",
        "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list_raw.txt",
        "https://raw.githubusercontent.com/LonUp/NodeList/main/V2RAY/Latest.txt",
        "https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/all",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Reality-Azadi-config/Config/Azadi-Reality-Different",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Reality-Azadi-config/Config/Config",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/MCI.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/Mobinet.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/Mokhabrat.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/Rightel.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/irancell.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/shatel.txt",
        "https://raw.githubusercontent.com/amirmohammad-mohammad-88/Sub-Config-operator/Config/various",
        "https://raw.githubusercontent.com/irancpi/Subscription/main/Sub",
        "https://raw.githubusercontent.com/rezaxanii/Config-Station/main/configs.txt",
        "https://branch.blanku.me",
        "https://raw.githubusercontent.com/halfaaa/Free/main/1.30.2023.txt",
    ]

    decoded_links = decode_links(links)
    decoded_dir_links = decode_dir_links(dir_links)

    combined_data = decoded_links + decoded_dir_links
    merged_configs = filter_for_protocols(combined_data, protocols)

    # Clean existing output files
    output_filename = os.path.join(output_folder, "All_Configs_Sub.txt")
    filename1 = os.path.join(output_folder, "All_Configs_base64_Sub.txt")
    
    if os.path.exists(output_filename):
        os.remove(output_filename)
    if os.path.exists(filename1):
        os.remove(filename1)

    for i in range(20):
        filename = os.path.join(output_folder, f"Sub{i}.txt")
        if os.path.exists(filename):
            os.remove(filename)
        filename1 = os.path.join(base64_folder, f"Sub{i}_base64.txt")
        if os.path.exists(filename1):
            os.remove(filename1)

    # Write merged configs to output file
    with open(output_filename, "w") as f:
        f.write(fixed_text)
        for config in merged_configs:
            f.write(config + "\n")

    # Split merged configs into smaller files (no more than 600 configs per file)
    with open(output_filename, "r") as f:
        lines = f.readlines()

    num_lines = len(lines)
    max_lines_per_file = 600
    num_files = (num_lines + max_lines_per_file - 1) // max_lines_per_file

    for i in range(num_files):
        profile_title = f"🆓 Git:Barry-far | Sub{i+1} 🫂"
        encoded_title = base64.b64encode(profile_title.encode()).decode()
        custom_fixed_text = f"""#profile-title: base64:{encoded_title}
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/coldwater-10/V2ray-Configs
#profile-web-page-url: https://github.com/coldwater-10/V2ray-Configs
"""

        input_filename = os.path.join(output_folder, f"Sub{i + 1}.txt")
        with open(input_filename, "w") as f:
            f.write(custom_fixed_text)
            start_index = i * max_lines_per_file
            end_index = min((i + 1) * max_lines_per_file, num_lines)
            for line in lines[start_index:end_index]:
                f.write(line)

        with open(input_filename, "r") as input_file:
            config_data = input_file.read()
        
        output_filename = os.path.join(base64_folder, f"Sub{i + 1}_base64.txt")
        with open(output_filename, "w") as output_file:
            encoded_config = base64.b64encode(config_data.encode()).decode()
            output_file.write(encoded_config)

if __name__ == "__main__":
    main()
