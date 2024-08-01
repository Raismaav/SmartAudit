from Controller import Controller

if __name__ == "__main__":
    file_path = 'files/factura.pdf'
    app_controller = Controller(file_path)
    app_controller.run()
