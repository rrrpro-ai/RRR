# Install libraries first: pip install flask flask-cors yt-dlp
from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app) # HTML ஃபைல் இதனுடன் பேச அனுமதி அளிக்கிறது

@app.route('/extract', methods=['POST'])
def extract_media():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({"success": False, "error": "No URL provided"})

    print(f"[RRR PRO MEX] Extracting: {url}")
    
    # yt-dlp options to extract BEST direct link without downloading to server
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Extracting the direct raw URL and title
            direct_url = info.get('url')
            title = info.get('title', 'RRR_Pro_Mex_Media')
            
            return jsonify({
                "success": True, 
                "title": title, 
                "direct_link": direct_url
            })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    print(">>> RRR PRO MEX OMEGA SERVER RUNNING ON PORT 5000 <<<")
    app.run(port=5000)