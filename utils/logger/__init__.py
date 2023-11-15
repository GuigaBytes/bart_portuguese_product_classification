# Definir códigos ANSI para cores
red_color = "\033[91m"
green_color = "\033[92m"
yellow_color = "\033[93m"
blue_color = "\033[0;34m"
reset_color = "\033[0m"

def log(text, color = blue_color):
  print(f"{color}{text}{reset_color}")

def info(text):
  log(text, blue_color)

def warning(text):
  log(text, yellow_color)

def success(text):
  log(text, green_color)

def danger(text):
  log(text, red_color)
