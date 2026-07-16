class VercelV0LayoutGeneratorClient:
    def get_layout(self, layout_prompt: str) -> dict:
        return {"component_markup": f"<div className='flex flex-col'>\n  {layout_prompt}\n</div>"}