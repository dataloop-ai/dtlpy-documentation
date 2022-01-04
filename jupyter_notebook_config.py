c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors self https://*.dataloop.ai:*"
        # 'Content-Security-Policy': "frame-ancestors self http://localhost:*"
    }
}

c.NotebookApp.allow_remote_access = True
c.NotebookApp.token = ''
c.NotebookApp.open_browser = False
c.NotebookApp.disable_check_xsrf = True