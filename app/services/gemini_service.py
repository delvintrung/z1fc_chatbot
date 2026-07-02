from google import genai
from app.config import GEMINI_API_KEY, CHAT_MODEL
from app.services.rag_service import search_context

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(message: str) -> str:
    context = search_context(message)

    prompt = f"""
Bạn là AI tư vấn sản phẩm ARZOPA Z1FC trên landing page.

Chỉ trả lời dựa trên CONTEXT bên dưới.
Nếu CONTEXT không có thông tin, hãy nói:
"Hiện tại mình chưa có đủ thông tin để trả lời chính xác câu này."

CONTEXT:
{context}

CÂU HỎI KHÁCH HÀNG:
{message}

Yêu cầu trả lời:
- Trả lời bằng tiếng Việt
- Ngắn gọn
- Tự nhiên
- Tập trung vào tư vấn sản phẩm
- Không bịa thông tin ngoài context
"""

    response = client.models.generate_content(
        model=CHAT_MODEL,
        contents=prompt,
    )

    return response.text or "Xin lỗi, hiện tại mình chưa thể trả lời."