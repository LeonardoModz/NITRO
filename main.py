import requests
from telethon import TelegramClient, events


api_id = '29317917'
api_hash = '22d0e195a4dc3b45d84f303d11ae6621'


client = TelegramClient('bot', api_id, api_hash)
def format_response(data):
    try:
        print(data)
        basic_info = data.get('basicInfo', {})
        profile_info = data.get('profileInfo', {})
        clan_info = data.get('clanBasicInfo', {})
        captain_info = data.get('captainBasicInfo', {})
        pet_info = data.get('petInfo', {})
        social_info = data.get('socialInfo', {})
        credit_score_info = data.get('creditScoreInfo', {})
        diamond_cost = data.get('diamondCostRes', {})

        def get_value(info, key, default="NÃO ENCONTRADO"):
            return info.get(key, default) if isinstance(info, dict) else default
        formatted_data = (
            "🎮 **LEO BOT BUSCAR INFORMAÇÕES FF** 🎮\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**👤 Account ID**: `{get_value(basic_info, 'accountId')}`\n"
            f"**🔤 Nickname**: `{get_value(basic_info, 'nickname')}`\n"
            f"**🌎 Region**: `{get_value(basic_info, 'region')}`\n"
            f"**⭐ Level**: `{get_value(basic_info, 'level')}`\n"
            f"**📊 Experience Points**: `{get_value(basic_info, 'exp')}`\n"
            f"**🏆 Rank**: `{get_value(basic_info, 'rank')}`\n"
            f"**🎖 Ranking Points**: `{get_value(basic_info, 'rankingPoints')}`\n"
            f"**💠 Badge Count**: `{get_value(basic_info, 'badgeCnt')}`\n"
            f"**🗓 Last Login**: `{get_value(basic_info, 'lastLoginAt')}`\n"
            f"**⚔️ Max Rank**: `{get_value(basic_info, 'maxRank')}`\n"
            f"**🛡 CS Rank**: `{get_value(basic_info, 'csRank')}`\n"
            f"**🔝 CS Max Rank**: `{get_value(basic_info, 'csMaxRank')}`\n"
            f"**🔺 Peak Rank Position**: `{get_value(basic_info, 'peakRankPos')}`\n"
            f"**🎮 Account Prefers**: `{get_value(basic_info.get('accountPrefers', {}), 'brPregameShowChoices')}`\n"
            f"**🔖 Title**: `{get_value(basic_info, 'title')}`\n"
            f"**🗓 Created At**: `{get_value(basic_info, 'createAt')}`\n"
            f"**🛠 Release Version**: `{get_value(basic_info, 'releaseVersion')}`\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            f"🛡 **Profile Info** 🛡\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**👤 Avatar ID**: `{get_value(profile_info, 'avatarId')}`\n"
            f"**👗 Clothes**: `{get_value(profile_info, 'clothes')}`\n"
            f"**🔫 PVE Primary Weapon**: `{get_value(profile_info, 'pvePrimaryWeapon')}`\n"
            f"**⏲ End Time**: `{get_value(profile_info, 'endTime')}`\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            "🏆 **Guild Information** 🏆\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**⚔️ Guild Name**: `{get_value(clan_info, 'clanName')}`\n"
            f"**🎯 Guild ID**: `{get_value(clan_info, 'clanId')}`\n"
            f"**🆙 Guild Level**: `{get_value(clan_info, 'clanLevel')}`\n"
            f"**👥 Members**: `{get_value(clan_info, 'memberNum')}/{get_value(clan_info, 'capacity')}`\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            "👑 **Captain Information** 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**🎮 Captain Nickname**: `{get_value(captain_info, 'nickname')}`\n"
            f"**⭐ Captain Level**: `{get_value(captain_info, 'level')}`\n"
            f"**🛡 Rank**: `{get_value(captain_info, 'rank')}`\n"
            f"**🎖 Ranking Points**: `{get_value(captain_info, 'rankingPoints')}`\n"
            f"**❤️ Likes**: `{get_value(captain_info, 'liked')}`\n"
            f"**⚔️ Max Rank**: `{get_value(captain_info, 'maxRank')}`\n"
            f"**🛡 CS Rank**: `{get_value(captain_info, 'csRank')}`\n"
            f"**🔝 CS Max Rank**: `{get_value(captain_info, 'csMaxRank')}`\n"
            f"**🗓 Created At**: `{get_value(captain_info, 'createAt')}`\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            "🐾 **Pet Information** 🐾\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**🐶 Pet Name**: `{get_value(pet_info, 'name')}`\n"
            f"**🆙 Pet Level**: `{get_value(pet_info, 'level')}`\n"
            f"**🔄 Experience**: `{get_value(pet_info, 'exp')}`\n"
            f"**✨ Selected Skill ID**: `{get_value(pet_info, 'selectedSkillId')}`\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            "📱 **Social Information** 📱\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**🔖 Gender**: `{get_value(social_info, 'gender')}`\n"
            f"**🌍 Language**: `{get_value(social_info, 'language')}`\n"
            f"**💬 Signature**: `{get_value(social_info, 'signature')}`\n"
            f"**🏅 Rank Show**: `{get_value(social_info, 'rankShow')}`\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            "💎 **Diamond Information** 💎\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**💎 Diamond Cost**: `{get_value(diamond_cost, 'diamondCost')}`\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            "✅ **Credit Score** ✅\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**💯 Credit Score**: `{get_value(credit_score_info, 'creditScore')}`\n"
            f"**📅 Summary Start**: `{get_value(credit_score_info, 'periodicSummaryStartTime')}`\n"
            f"**📅 Summary End**: `{get_value(credit_score_info, 'periodicSummaryEndTime')}`\n"
            f"**👍 Likes in Period**: `{get_value(credit_score_info, 'periodicSummaryLikeCnt')}`\n"
            "━━━━━━━━━━━━━━━━━━━━━━"
        )
        return formatted_data
    except KeyError:
        return "❌ CONTA INEXISTENTE OU ID INVÁLIDO ❔"
def get_region_and_id(account_id):
    url = 'https://recargajogo.com.br/api/auth/player_id_login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; moto g22 Build/STAS32.79-77-28-63-3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Mobile Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?1',
        'Origin': 'https://recargajogo.com.br',
        'X-Requested-With': 'mark.via.gp',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://recargajogo.com.br/',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'source=mb; region=BR; mspid2=697c9e284e00ac32b36ba324b1f4f3cb; cc=true; datadome=r2V64Wrv_3eLPO80qhUWDIddDTPv5htTiIcL78574qqpKsnNQkJT5wuuPM2HjMVExS4~2o54Z0JF3BIWjuFiVXfiIcNQ6hV~NVCrp5dE_BgoJJLXtPmT14tayARU7jzj; session_key=lp9h69jq5xrg6sq3eatfuzb9roiukc3c'
    }
    payload = {"app_id": 100067, "login_id": account_id}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data['region'], account_id
    else:
        return None, None
def get_ff_account_data(region, account_id):
    url = f"https://free-ff-api-src-5plp.onrender.com/api/v1/account?region={region}&uid={account_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return format_response(data)
    else:
        return "❌ NÃO EXISTE CONTA ❔"
@client.on(events.NewMessage(pattern=r'/ff (\d+)'))
async def handler(event):
    account_id = event.pattern_match.group(1)
    region, open_id = get_region_and_id(account_id)
    if region and open_id:
        response = get_ff_account_data(region, open_id)
        await event.reply(response)
    else:
        await event.reply("❌ ERRO AO BUSCAR ❔")
client.start()
client.run_until_disconnected()