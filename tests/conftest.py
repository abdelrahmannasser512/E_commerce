import pytest
import selenium.webdriver as wd
import json
@pytest.fixture

def browser(config):
    if config['browser']=='Chrome':
        b=wd.Chrome()
    elif config['browser']=='Firefox':
        b=wd.Firefox()
    elif config['browser']=='Headless Chrome':
        options=wd.ChromeOptions()
        options.add_argument('headless')
        b=wd.Chrome(options=options)
    else:
        raise Exception (f'browser {config["browser"]} , not indicated ')
    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit

@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config=json.load(config_file)
    assert config['browser'] in ['Chrome','Firefox','Headless Chrome']
    assert isinstance(config['implicit_wait'],int)
    assert config['implicit_wait']>0
    
    return config
