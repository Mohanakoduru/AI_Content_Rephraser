def build_prompt(user_text):
    return f"""
You are a professional copywriter and content strategist.

Rewrite the content below into EXACTLY five versions.

STRICT RULES:
- Output ONLY what is requested
- DO NOT add explanations
- DO NOT add notes
- DO NOT add extra sections
- DO NOT use markdown (**)
- Each section MUST start with the exact label below
- Each section MUST end with <<<END>>>

FORMAT (MUST FOLLOW EXACTLY):

VIRAL:
<text>
<<<END>>>

SHORT:
<text>
<<<END>>>

EMOTIONAL:
<text>
<<<END>>>

SEO:
<text>
<<<END>>>

KPOP:
<text>
<<<END>>>

CONTENT:
"{user_text}"
"""
