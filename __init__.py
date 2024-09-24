from .nodes.FL_Image_Randomizer import FL_ImageRandomizer
from .nodes.FL_Image_Caption_Saver import FL_ImageCaptionSaverABC
from .nodes.FL_Image_Dimension_Display import FL_ImageDimensionDisplay
from .nodes.FL_Code_Node import FL_CodeNode
from .nodes.FL_Image_Pixelator import FL_ImagePixelator
from .nodes.FL_DirectoryCrawl import FL_DirectoryCrawl
from .nodes.FL_Ascii import FL_Ascii
from .nodes.FL_Glitch import FL_Glitch
from .nodes.FL_Ripple import FL_Ripple
from .nodes.FL_PixelSort import FL_PixelSort
from .nodes.FL_HexagonalPattern import FL_HexagonalPattern
from .nodes.FL_NFTGenerator import FL_NFTGenerator
from .nodes.FL_HalfTone import FL_HalftonePattern
from .nodes.FL_RandomRange import FL_RandomNumber
from .nodes.FL_PromptSelector import FL_PromptSelector
from .nodes.FL_Shader import FL_Shadertoy
from .nodes.FL_PixelArt import FL_PixelArtShader
from .nodes.FL_InfiniteZoom import FL_InfiniteZoom
from .nodes.FL_PaperDrawn import FL_PaperDrawn
from .nodes.FL_ImageNotes import FL_ImageNotes
from .nodes.FL_ImageCollage import FL_ImageCollage
from .nodes.FL_KsamplerSettings import FL_KsamplerSettings
from .nodes.FL_RetroEffect import FL_RetroEffect
from .nodes.FL_InpaintCrop import FL_InpaintCrop
from .nodes.FL_InpaintCrop import FL_Inpaint_Stitch
from .nodes.FL_SD_Slices import FL_SDUltimate_Slices
from .nodes.FL_BatchAligned import FL_BatchAlign
from .nodes.FL_VideoCropNStitch import FL_VideoCropMask
from .nodes.FL_VideoCropNStitch import FL_VideoRecompose
from .nodes.FL_SeparateMasks import FL_SeparateMaskComponents
from .nodes.FL_PasteOnCanvas import FL_PasteOnCanvas
from .nodes.FL_BulletHellGame import FL_BulletHellGame
from .nodes.FL_TetrisGame import FL_TetrisGame
from .nodes.FL_Dither import FL_Dither
from .nodes.FL_SystemCheck import FL_SystemCheck
from .nodes.FL_ColorPicker import FL_ColorPicker
from .nodes.FL_GradGen import FL_GradGenerator
from .nodes.FL_MirrorAndAppendCaptions import FL_MirrorAndAppendCaptions
from .nodes.FL_ImageCaptionLayout import FL_ImageCaptionLayout
from .nodes.FL_HFHubModelUploader import FL_HFHubModelUploader
from .nodes.FL_ZipDirectory import FL_ZipDirectory
from .nodes.FL_ZipSave import FL_ZipSave
from .nodes.FL_GPT_Vision import FL_GPT_Vision
from .nodes.FL_TimeLine import FL_TimeLine
from .nodes.FL_SimpleGPTVision import FL_SimpleGPTVision
from .nodes.FL_DiscordWebhook import FL_SendToDiscordWebhook
from .nodes.FL_HF_Character import FL_HF_Character
from .nodes.FL_CaptionToCSV import FL_CaptionToCSV
from .nodes.FL_KsamplerPlus import FL_KsamplerPlus
from .nodes.FL_KsamplerBasic import FL_KsamplerBasic
from .nodes.FL_KsamplerFractals import FL_FractalKSampler
from .nodes.FL_UpscaleModel import FL_UpscaleModel
from .nodes.FL_SaveCSV import FL_SaveCSV
from. nodes.FL_KSamplerXYZPlot import FL_KSamplerXYZPlot
from .nodes.FL_SamplerStrings import FL_SamplerStrings
from .nodes.FL_SchedulerStrings import FL_SchedulerStrings
from .nodes.FL_ImageCaptionLayoutPDF import FL_ImageCaptionLayoutPDF
from .nodes.FL_Dalle3 import FL_Dalle3
from .nodes.FL_SaveImages import FL_SaveImages
from .nodes.FL_LoadImage import FL_LoadImage
from .nodes.FL_PDFLoader import FL_PDFLoader
from .nodes.FL_PDFToImage import FL_PDFToImages
from .nodes.FL_PDFSaver import FL_PDFSaver
from .nodes.FL_ImagesToPDF import FL_ImagesToPDF
from .nodes.FL_PDFMerger import FL_PDFMerger
from .nodes.FL_PDFTextExtractor import FL_PDFTextExtractor
from .nodes.FL_PDFImageExtractor import FL_PDFImageExtractor
from .nodes.FL_BulkPDFLoader import FL_BulkPDFLoader
from .nodes.FL_SaveAndDisplayImage import FL_SaveAndDisplayImage
from .nodes.FL_OllamaCaptioner import FL_OllamaCaptioner
from .nodes.FL_ImageAdjuster import FL_ImageAdjuster




NODE_CLASS_MAPPINGS = {
    "FL_ImageRandomizer": FL_ImageRandomizer,
    "FL_ImageCaptionSaverABC": FL_ImageCaptionSaverABC,
    "FL_ImageDimensionDisplay": FL_ImageDimensionDisplay,
    "FL_CodeNode": FL_CodeNode,
    "FL_ImagePixelator": FL_ImagePixelator,
    "FL_DirectoryCrawl": FL_DirectoryCrawl,
    "FL_Ascii": FL_Ascii,
    "FL_Glitch": FL_Glitch,
    "FL_Ripple": FL_Ripple,
    "FL_PixelSort": FL_PixelSort,
    "FL_HexagonalPattern": FL_HexagonalPattern,
    "FL_NFTGenerator": FL_NFTGenerator,
    "FL_HalftonePattern": FL_HalftonePattern,
    "FL_RandomNumber": FL_RandomNumber,
    "FL_PromptSelector": FL_PromptSelector,
    "FL_Shadertoy": FL_Shadertoy,
    "FL_PixelArtShader": FL_PixelArtShader,
    "FL_InfiniteZoom": FL_InfiniteZoom,
    "FL_PaperDrawn": FL_PaperDrawn,
    "FL_ImageNotes": FL_ImageNotes,
    "FL_ImageCollage": FL_ImageCollage,
    "FL_KsamplerSettings": FL_KsamplerSettings,
    "FL_RetroEffect": FL_RetroEffect,
    "FL_InpaintCrop": FL_InpaintCrop,
    "FL_Inpaint_Stitch": FL_Inpaint_Stitch,
    "FL_SDUltimate_Slices": FL_SDUltimate_Slices,
    "FL_BatchAlign": FL_BatchAlign,
    "FL_VideoRecompose": FL_VideoRecompose,
    "FL_VideoCropMask": FL_VideoCropMask,
    "FL_SeparateMaskComponents": FL_SeparateMaskComponents,
    "FL_PasteOnCanvas": FL_PasteOnCanvas,
    "FL_BulletHellGame": FL_BulletHellGame,
    "FL_TetrisGame": FL_TetrisGame,
    "FL_Dither": FL_Dither,
    "FL_SystemCheck": FL_SystemCheck,
    "FL_ColorPicker": FL_ColorPicker,
    "FL_GradGenerator": FL_GradGenerator,
    "FL_MirrorAndAppendCaptions": FL_MirrorAndAppendCaptions,
    "FL_ImageCaptionLayout": FL_ImageCaptionLayout,
    "FL_HFHubModelUploader": FL_HFHubModelUploader,
    "FL_ZipDirectory": FL_ZipDirectory,
    "FL_ZipSave": FL_ZipSave,
    "FL_GPT_Vision": FL_GPT_Vision,
    "FL_TimeLine": FL_TimeLine,
    "FL_SimpleGPTVision": FL_SimpleGPTVision,
    "FL_SendToDiscordWebhook": FL_SendToDiscordWebhook,
    "FL_HF_Character": FL_HF_Character,
    "FL_CaptionToCSV": FL_CaptionToCSV,
    "FL_KsamplerPlus": FL_KsamplerPlus,
    "FL_KsamplerBasic": FL_KsamplerBasic,
    "FL_FractalKSampler": FL_FractalKSampler,
    "FL_UpscaleModel": FL_UpscaleModel,
    "FL_SaveCSV": FL_SaveCSV,
    "FL_KSamplerXYZPlot": FL_KSamplerXYZPlot,
    "FL_SamplerStrings": FL_SamplerStrings,
    "FL_SchedulerStrings": FL_SchedulerStrings,
    "FL_ImageCaptionLayoutPDF": FL_ImageCaptionLayoutPDF,
    "FL_Dalle3": FL_Dalle3,
    "FL_SaveImages": FL_SaveImages,
    "FL_LoadImage": FL_LoadImage,
    "FL_PDFLoader": FL_PDFLoader,
    "FL_PDFToImages": FL_PDFToImages,
    "FL_PDFSaver": FL_PDFSaver,
    "FL_ImagesToPDF": FL_ImagesToPDF,
    "FL_PDFMerger": FL_PDFMerger,
    "FL_PDFTextExtractor": FL_PDFTextExtractor,
    "FL_PDFImageExtractor": FL_PDFImageExtractor,
    "FL_BulkPDFLoader": FL_BulkPDFLoader,
    "FL_SaveAndDisplayImage": FL_SaveAndDisplayImage,
    "FL_OllamaCaptioner": FL_OllamaCaptioner,
    "FL_ImageAdjuster": FL_ImageAdjuster,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FL_ImageRandomizer": "FL Image Randomizer",
    "FL_ImageCaptionSaverABC": "FL Image Caption Saver",
    "FL_ImageDimensionDisplay": "FL Image Size",
    "FL_CodeNode": "FL Code Node",
    "FL_ImagePixelator": "FL Image Pixelator",
    "FL_DirectoryCrawl": "FL Directory Crawl",
    "FL_Ascii": "FL Ascii",
    "FL_Glitch": "FL Glitch",
    "FL_Ripple": "FL Ripple",
    "FL_PixelSort": "FL PixelSort",
    "FL_HexagonalPattern": "FL Hexagonal Pattern",
    "FL_NFTGenerator": "FL NFT Generator",
    "FL_HalftonePattern": "FL Halftone",
    "FL_RandomNumber": "FL Random Number",
    "FL_PromptSelector": "FL Prompt Selector",
    "FL_Shadertoy": "FL Shadertoy",
    "FL_PixelArtShader": "FL Pixel Art",
    "FL_InfiniteZoom": "FL Infinite Zoom",
    "FL_PaperDrawn": "FL Paper Drawn",
    "FL_ImageNotes": "FL Image Notes",
    "FL_ImageCollage": "FL Image Collage",
    "FL_KsamplerSettings": "FL KSampler Settings",
    "FL_RetroEffect": "FL Retro Effect",
    "FL_InpaintCrop": "FL Inpaint Crop",
    "FL_Inpaint_Stitch": "FL Inpaint Stitch",
    "FL_SDUltimate_Slices": "FL SDUltimate Slices",
    "FL_BatchAlign": "FL Batch Align",
    "FL_VideoCropMask": "FL Video CropMask",
    "FL_VideoRecompose": "FL Video Recompose",
    "FL_SeparateMaskComponents": "FL Separate Mask Components",
    "FL_PasteOnCanvas": "FL Paste On Canvas",
    "FL_BulletHellGame": "FL BulletHell Game",
    "FL_TetrisGame": "FL Tetris Game",
    "FL_Dither": "FL Dither",
    "FL_SystemCheck": "FL System Check",
    "FL_ColorPicker": "FL Color Picker",
    "FL_GradGenerator": "FL Grad Generator",
    "FL_MirrorAndAppendCaptions": "FL Mirror And Append Captions",
    "FL_ImageCaptionLayout": "FL Image Caption Layout",
    "FL_HFHubModelUploader": "FL HFHub Model Uploader",
    "FL_ZipDirectory": "FL Zip Directory",
    "FL_ZipSave": "FL_ZipSave",
    "FL_GPT_Vision": "FL GPT Captions",
    "FL_TimeLine": "FL Time Line",
    "FL_SimpleGPTVision": "FL Simple GPT Vision",
    "FL_SendToDiscordWebhook": "FL Kytra Discord Webhook",
    "FL_HF_Character": "FL HF Character",
    "FL_CaptionToCSV": "FL Caption To CSV",
    "FL_KsamplerPlus": "FL KSampler Plus",
    "FL_KsamplerBasic": "FL KSampler Basic",
    "FL_FractalKSampler": "FL Fractal KSampler",
    "FL_UpscaleModel": "FL Upscale Model",
    "FL_SaveCSV": "FL Save CSV",
    "FL_KSamplerXYZPlot": "FL KSampler XYZ Plot",
    "FL_SamplerStrings": "FL Sampler String XYZ",
    "FL_SchedulerStrings": "FL Scheduler String XYZ",
    "FL_ImageCaptionLayoutPDF": "FL Image Caption Layout PDF",
    "FL_Dalle3": "FL Dalle 3",
    "FL_SaveImages": "FL Save Images",
    "FL_LoadImage": "FL Load Image",
    "FL_PDFLoader": "FL PDF Loader",
    "FL_PDFToImages": "FL PDF To Images",
    "FL_PDFSaver": "FL PDF Saver",
    "FL_ImagesToPDF": "FL Images To PDF",
    "FL_PDFMerger": "FL PDF Merger",
    "FL_PDFTextExtractor": "FL PDF Text Extractor",
    "FL_PDFImageExtractor": "FL PDF Image Extractor",
    "FL_BulkPDFLoader": "FL Bulk PDF Loader",
    "FL_SaveAndDisplayImage": "FL Save And Display Image",
    "FL_OllamaCaptioner": "FL Ollama Captioner by Cosmic",
    "FL_ImageAdjuster": "FL_ImageAdjuster",

}


ascii_art = """

███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗               
████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝               
██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗                 
██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝                 
██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗               
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝               
                                                                       
██████╗ ███████╗██╗     ██╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔════╝██║     ██║   ██║██╔════╝██║██╔═══██╗████╗  ██║██╔════╝
██║  ██║█████╗  ██║     ██║   ██║███████╗██║██║   ██║██╔██╗ ██║███████╗
██║  ██║██╔══╝  ██║     ██║   ██║╚════██║██║██║   ██║██║╚██╗██║╚════██║
██████╔╝███████╗███████╗╚██████╔╝███████║██║╚██████╔╝██║ ╚████║███████║
╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                                       

"""
print(ascii_art)

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
