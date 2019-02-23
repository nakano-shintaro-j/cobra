from lazyme.string import color_print
import json
import yaml
import sys


class CobraConfiguration:

    def __init__(self):
        pass

    def cobra_print(self, text, color=None, bold=False, background=None, underline=False):
        if color == 'success':
            return color_print(text, color='green', bold=bold, highlighter=background, underline=underline)
        elif color == 'warning':
            return color_print(text, color='yellow', bold=bold, highlighter=background, underline=underline)
        elif color == 'error':
            return color_print(text, color='red', bold=bold, highlighter=background, underline=underline)
        else:
            return color_print(text, bold=bold, highlighter=background, underline=underline)

    def file_reader(self, file):
        try:
            with open(file, 'r') as read_file:
                return_file = read_file.read()
                read_file.close()
                return return_file
        except FileNotFoundError:
            self.cobra_print("[Cobra] FileNotFound: %s" % file, "error", bold=True)
        sys.exit()

    def yaml_loader(self, yaml_file):
        try:
            load_compile = yaml.load(yaml_file)
            return load_compile
        except yaml.scanner.ScannerError as scannerError:
            self.cobra_print("[Cobra] YAMLScannerError: %s" % scannerError, "error", bold=True)
        sys.exit()

    def json_loader(self, json_file):
        try:
            loaded_json = json.loads(json_file)
            return loaded_json
        except json.decoder.JSONDecodeError as jsonDecodeError:
            self.cobra_print("[Cobra] JSONDecodeError: %s" % jsonDecodeError, "error", bold=True)
        sys.exit()

    def compile(self, compile_yaml):
        compiles = []
        try:
            if compile_yaml['solidity_path_dir'] and compile_yaml['contracts']:
                artifact_path_dir = None
                try:
                    if compile_yaml['artifact_path_dir']:
                        artifact_path_dir = compile_yaml['artifact_path_dir']
                except KeyError:
                    self.cobra_print("[WARNING] Cobra: Can't find artifact_path_dir. "
                                     "By default ./build/contracts", "warning", bold=True)
                for contract in compile_yaml['contracts']:
                    try:
                        if contract['contract']['solidity']:
                            try:
                                if contract['contract']['links_path_dir']:
                                    try:
                                        if contract['contract']['solidity_path_dir']:
                                            try:
                                                if contract['contract']['remappings']:
                                                    compiles.append(dict(
                                                        solidity_path_dir=contract['contract']['solidity_path_dir'],
                                                        solidity=contract['contract']['solidity'],
                                                        links_path_dir=contract['contract']['links_path_dir'],
                                                        artifact_path_dir=artifact_path_dir,
                                                        remappings=contract['contract']['remappings']
                                                    ))
                                                    continue
                                                elif not contract['contract']['remappings']:
                                                    compiles.append(dict(
                                                        solidity_path_dir=contract['contract']['solidity_path_dir'],
                                                        solidity=contract['contract']['solidity'],
                                                        links_path_dir=contract['contract']['links_path_dir'],
                                                        artifact_path_dir=artifact_path_dir,
                                                        remappings=None
                                                    ))
                                                    continue
                                            except KeyError:
                                                compiles.append(dict(
                                                    solidity_path_dir=contract['contract']['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=contract['contract']['links_path_dir'],
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=None
                                                ))
                                                continue
                                        elif not contract['contract']['solidity_path_dir']:
                                            try:
                                                if contract['contract']['remappings']:
                                                    compiles.append(dict(
                                                        solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                        solidity=contract['contract']['solidity'],
                                                        links_path_dir=contract['contract']['links_path_dir'],
                                                        artifact_path_dir=artifact_path_dir,
                                                        remappings=contract['contract']['remappings']
                                                    ))
                                                    continue
                                                elif not contract['contract']['remappings']:
                                                    compiles.append(dict(
                                                        solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                        solidity=contract['contract']['solidity'],
                                                        links_path_dir=contract['contract']['links_path_dir'],
                                                        artifact_path_dir=artifact_path_dir,
                                                        remappings=None
                                                    ))
                                                    continue
                                            except KeyError:
                                                compiles.append(dict(
                                                    solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=contract['contract']['links_path_dir'],
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=None
                                                ))
                                                continue
                                    except KeyError:
                                        try:
                                            if contract['contract']['remappings']:
                                                compiles.append(dict(
                                                    solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=contract['contract']['links_path_dir'],
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=contract['contract']['remappings']
                                                ))
                                                continue
                                            elif not contract['contract']['remappings']:
                                                compiles.append(dict(
                                                    solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=contract['contract']['links_path_dir'],
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=None
                                                ))
                                                continue
                                        except KeyError:
                                            compiles.append(dict(
                                                solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                solidity=contract['contract']['solidity'],
                                                links_path_dir=contract['contract']['links_path_dir'],
                                                artifact_path_dir=artifact_path_dir,
                                                remappings=None
                                            ))
                                            continue
                                elif not contract['contract']['links_path_dir']:
                                    try:
                                        if contract['contract']['solidity_path_dir']:
                                            try:
                                                if contract['contract']['remappings']:
                                                    compiles.append(dict(
                                                        solidity_path_dir=contract['contract']['solidity_path_dir'],
                                                        solidity=contract['contract']['solidity'],
                                                        links_path_dir=None,
                                                        artifact_path_dir=artifact_path_dir,
                                                        remappings=contract['contract']['remappings']
                                                    ))
                                                    continue
                                                elif not contract['contract']['remappings']:
                                                    compiles.append(dict(
                                                        solidity_path_dir=contract['contract']['solidity_path_dir'],
                                                        solidity=contract['contract']['solidity'],
                                                        links_path_dir=None,
                                                        artifact_path_dir=artifact_path_dir,
                                                        remappings=None
                                                    ))
                                                    continue
                                            except KeyError:
                                                compiles.append(dict(
                                                    solidity_path_dir=contract['contract']['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=None,
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=None
                                                ))
                                                continue
                                        elif not contract['contract']['solidity_path_dir']:
                                            try:
                                                if contract['contract']['remappings']:
                                                    compiles.append(dict(
                                                        solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                        solidity=contract['contract']['solidity'],
                                                        links_path_dir=None,
                                                        artifact_path_dir=artifact_path_dir,
                                                        remappings=contract['contract']['remappings']
                                                    ))
                                                    continue
                                                elif not contract['contract']['remappings']:
                                                    compiles.append(dict(
                                                        solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                        solidity=contract['contract']['solidity'],
                                                        links_path_dir=None,
                                                        artifact_path_dir=artifact_path_dir,
                                                        remappings=None
                                                    ))
                                                    continue
                                            except KeyError:
                                                compiles.append(dict(
                                                    solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=None,
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=None
                                                ))
                                                continue
                                    except KeyError:
                                        try:
                                            if contract['contract']['remappings']:
                                                compiles.append(dict(
                                                    solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=None,
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=contract['contract']['remappings']
                                                ))
                                                continue
                                            elif not contract['contract']['remappings']:
                                                compiles.append(dict(
                                                    solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=None,
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=None
                                                ))
                                                continue
                                        except KeyError:
                                            compiles.append(dict(
                                                solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                solidity=contract['contract']['solidity'],
                                                links_path_dir=None,
                                                artifact_path_dir=artifact_path_dir,
                                                remappings=None
                                            ))
                                            continue
                            except KeyError:
                                try:
                                    if contract['contract']['solidity_path_dir']:
                                        try:
                                            if contract['contract']['remappings']:
                                                compiles.append(dict(
                                                    solidity_path_dir=contract['contract']['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=None,
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=contract['contract']['remappings']
                                                ))
                                                continue
                                            elif not contract['contract']['remappings']:
                                                compiles.append(dict(
                                                    solidity_path_dir=contract['contract']['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=None,
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=None
                                                ))
                                                continue
                                        except KeyError:
                                            compiles.append(dict(
                                                solidity_path_dir=contract['contract']['solidity_path_dir'],
                                                solidity=contract['contract']['solidity'],
                                                links_path_dir=None,
                                                artifact_path_dir=artifact_path_dir,
                                                remappings=None
                                            ))
                                            continue
                                    elif not contract['contract']['solidity_path_dir']:
                                        try:
                                            if contract['contract']['remappings']:
                                                compiles.append(dict(
                                                    solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=None,
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=contract['contract']['remappings']
                                                ))
                                                continue
                                            elif not contract['contract']['remappings']:
                                                compiles.append(dict(
                                                    solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                    solidity=contract['contract']['solidity'],
                                                    links_path_dir=None,
                                                    artifact_path_dir=artifact_path_dir,
                                                    remappings=None
                                                ))
                                                continue
                                        except KeyError:
                                            compiles.append(dict(
                                                solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                solidity=contract['contract']['solidity'],
                                                links_path_dir=None,
                                                artifact_path_dir=artifact_path_dir,
                                                remappings=None
                                            ))
                                            continue
                                except KeyError:
                                    try:
                                        if contract['contract']['remappings']:
                                            compiles.append(dict(
                                                solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                solidity=contract['contract']['solidity'],
                                                links_path_dir=None,
                                                artifact_path_dir=artifact_path_dir,
                                                remappings=contract['contract']['remappings']
                                            ))
                                            continue
                                        elif not contract['contract']['remappings']:
                                            compiles.append(dict(
                                                solidity_path_dir=compile_yaml['solidity_path_dir'],
                                                solidity=contract['contract']['solidity'],
                                                links_path_dir=None,
                                                artifact_path_dir=artifact_path_dir,
                                                remappings=None
                                            ))
                                            continue
                                    except KeyError:
                                        compiles.append(dict(
                                            solidity_path_dir=compile_yaml['solidity_path_dir'],
                                            solidity=contract['contract']['solidity'],
                                            links_path_dir=None,
                                            artifact_path_dir=artifact_path_dir,
                                            remappings=None
                                        ))
                                        continue
                    except KeyError:
                        self.cobra_print("[ERROR] Cobra: There is no solidity in contract.", "error", bold=True)
                        sys.exit()
        except KeyError:
            self.cobra_print("[ERROR] Cobra: Can't find solidity_path_dir or contracts in compile [cobra.yaml]", "error", bold=True)
            sys.exit()
        return compiles

    def deploy(self, deploy_yaml):
        deploys = []
        try:
            if deploy_yaml['artifact_path_dir'] and deploy_yaml['contracts']:
                for contract in deploy_yaml['contracts']:
                    try:
                        if contract['contract']['artifact']:
                            try:
                                if contract['contract']['links']:
                                    deploys.append(dict(
                                        artifact_path_dir=deploy_yaml['artifact_path_dir'],
                                        artifact=contract['contract']['artifact'],
                                        links=contract['contract']['links']
                                    ))
                                elif not contract['contract']['links']:
                                    deploys.append(dict(
                                        artifact_path_dir=deploy_yaml['artifact_path_dir'],
                                        artifact=contract['contract']['artifact'],
                                        links=None
                                    ))
                                    continue
                            except KeyError:
                                deploys.append(dict(
                                    artifact_path_dir=deploy_yaml['artifact_path_dir'],
                                    artifact=contract['contract']['artifact'],
                                    links=None
                                ))
                    except KeyError:
                        self.cobra_print("[ERROR] Cobra: There is no artifact in contract.", "error", bold=True)
                        sys.exit()
        except KeyError:
            self.cobra_print("[ERROR] Cobra: Can't find artifact_path_dir or contracts in deploy [cobra.yaml]", "error", bold=True)
            sys.exit()
        return deploys

    def test(self, test_yaml):
        tests = []
        try:
            if test_yaml['artifact_path_dir'] and test_yaml['contracts']:
                for contract in test_yaml['contracts']:
                    try:
                        if contract['contract']['artifact']:
                            try:
                                if contract['contract']['links']:
                                    tests.append(dict(
                                        artifact_path_dir=test_yaml['artifact_path_dir'],
                                        artifact=contract['contract']['artifact'],
                                        links=contract['contract']['links']
                                    ))
                                elif not contract['contract']['links']:
                                    tests.append(dict(
                                        artifact_path_dir=test_yaml['artifact_path_dir'],
                                        artifact=contract['contract']['artifact'],
                                        links=None
                                    ))
                                    continue
                            except KeyError:
                                tests.append(dict(
                                    artifact_path_dir=test_yaml['artifact_path_dir'],
                                    artifact=contract['contract']['artifact'],
                                    links=None
                                ))
                    except KeyError:
                        self.cobra_print("[ERROR] Cobra: There is no artifact in contract.", "error", bold=True)
                        sys.exit()
        except KeyError:
            self.cobra_print("[ERROR] Cobra: Can't find artifact_path_dir or contracts in test [cobra.yaml]", "error",
                             bold=True)
            sys.exit()
        return tests

    def account(self, account_yaml):
        if 'address' in account_yaml:
            if 'gas' in account_yaml:
                return dict(account=dict(
                    address=account_yaml['address'],
                    gas=account_yaml['gas']
                ))
            else:
                return dict(account=dict(
                    address=account_yaml['address']
                ))
        elif 'gas' in account_yaml:
            return dict(account=dict(
                gas=account_yaml['gas']
            ))
        else:
            self.cobra_print("[ERROR] Cobra: There is no address/gas in account.", "error", bold=True)
            sys.exit()

    def hdwallet(self, hdwallet_yaml):
        if 'mnemonic' in hdwallet_yaml or \
                'seed' in hdwallet_yaml or \
                'private' in hdwallet_yaml:
            # returns Mnemonic and Password
            if 'mnemonic' in hdwallet_yaml and 'password' in hdwallet_yaml:
                return dict(hdwallet=dict(
                    mnemonic=hdwallet_yaml['mnemonic'],
                    password=hdwallet_yaml['password']
                ))
            # returns Mnemonic
            elif 'mnemonic' in hdwallet_yaml:
                return dict(hdwallet=dict(
                    mnemonic=hdwallet_yaml['mnemonic']
                ))
            # returns Mnemonic (Seed is alias Mnemonic) and Password
            if 'seed' in hdwallet_yaml and 'password' in hdwallet_yaml:
                return dict(hdwallet=dict(
                    mnemonic=hdwallet_yaml['seed'],
                    password=hdwallet_yaml['password']
                ))
            # returns Mnemonic (Seed is alias Mnemonic)
            elif 'seed' in hdwallet_yaml:
                return dict(hdwallet=dict(
                    mnemonic=hdwallet_yaml['seed']
                ))
            # returns Private Key
            if 'private' in hdwallet_yaml:
                return dict(hdwallet=dict(
                    private=hdwallet_yaml['private']
                ))
        else:
            self.cobra_print("[ERROR] Cobra: There is no mnemonic(seed)/private in hdwallet.", "error", bold=True)
            sys.exit()

    def network(self, network_yaml):
        if 'development' in network_yaml:
            if 'host' in network_yaml['development'] or \
                    'url' in network_yaml['development']:
                if 'host' in network_yaml['development']:
                    if 'port' in network_yaml['development']:
                        # Protocol
                        if 'protocol' in network_yaml['development']:

                            if 'hdwallet' in network_yaml['development']:
                                __ = dict(
                                    host=network_yaml['development']['host'],
                                    port=network_yaml['development']['port'],
                                    protocol=network_yaml['development']['protocol']
                                )
                                hdwallet = self.hdwallet(network_yaml['development']['hdwallet'])
                                return {**__, **hdwallet}
                            elif 'account' in network_yaml['development']:
                                __ = dict(
                                    host=network_yaml['development']['host'],
                                    port=network_yaml['development']['port'],
                                    protocol=network_yaml['development']['protocol']
                                )
                                account = self.account(network_yaml['development']['account'])
                                return {**__, **account}
                            else:
                                return dict(
                                    host=network_yaml['development']['host'],
                                    port=network_yaml['development']['port'],
                                    protocol=network_yaml['development']['protocol']
                                )
                        # No Protocol
                        else:
                            if 'hdwallet' in network_yaml['development']:
                                __ = dict(
                                    host=network_yaml['development']['host'],
                                    port=network_yaml['development']['port']
                                )
                                hdwallet = self.hdwallet(network_yaml['development']['hdwallet'])
                                return {**__, **hdwallet}
                            elif 'account' in network_yaml['development']:
                                __ = dict(
                                    host=network_yaml['development']['host'],
                                    port=network_yaml['development']['port']
                                )
                                account = self.account(network_yaml['development']['account'])
                                return {**__, **account}
                            else:
                                return dict(
                                    host=network_yaml['development']['host'],
                                    port=network_yaml['development']['port']
                                )
                    else:
                        self.cobra_print("[ERROR] Cobra: There is no port in %s when you are using host."
                                         % 'development', "error", bold=True)
                        sys.exit()
                elif 'url' in network_yaml['development']:
                    # Port
                    if 'port' in network_yaml['development']:
                        # Protocol
                        if 'protocol' in network_yaml['development']:

                            if 'hdwallet' in network_yaml['development']:
                                __ = dict(
                                    url=network_yaml['development']['url'],
                                    port=network_yaml['development']['port'],
                                    protocol=network_yaml['development']['protocol']
                                )
                                hdwallet = self.hdwallet(network_yaml['development']['hdwallet'])
                                return {**__, **hdwallet}
                            elif 'account' in network_yaml['development']:
                                __ = dict(
                                    url=network_yaml['development']['url'],
                                    port=network_yaml['development']['port'],
                                    protocol=network_yaml['development']['protocol']
                                )
                                account = self.account(network_yaml['development']['account'])
                                return {**__, **account}
                            else:
                                return dict(
                                    url=network_yaml['development']['url'],
                                    port=network_yaml['development']['port'],
                                    protocol=network_yaml['development']['protocol']
                                )
                        # No Protocol
                        else:
                            if 'hdwallet' in network_yaml['development']:
                                __ = dict(
                                    url=network_yaml['development']['url'],
                                    port=network_yaml['development']['port']
                                )
                                hdwallet = self.hdwallet(network_yaml['development']['hdwallet'])
                                return {**__, **hdwallet}
                            elif 'account' in network_yaml['development']:
                                __ = dict(
                                    url=network_yaml['development']['url'],
                                    port=network_yaml['development']['port']
                                )
                                account = self.account(network_yaml['development']['account'])
                                return {**__, **account}
                            else:
                                return dict(
                                    url=network_yaml['development']['url'],
                                    port=network_yaml['development']['port']
                                )
                    # No Port
                    else:
                        # Protocol
                        if 'protocol' in network_yaml['development']:

                            if 'hdwallet' in network_yaml['development']:
                                __ = dict(
                                    url=network_yaml['development']['url'],
                                    protocol=network_yaml['development']['protocol']
                                )
                                hdwallet = self.hdwallet(network_yaml['development']['hdwallet'])
                                return {**__, **hdwallet}
                            elif 'account' in network_yaml['development']:
                                __ = dict(
                                    url=network_yaml['development']['url'],
                                    protocol=network_yaml['development']['protocol']
                                )
                                account = self.account(network_yaml['development']['account'])
                                return {**__, **account}
                            else:
                                return dict(
                                    url=network_yaml['development']['url'],
                                    protocol=network_yaml['development']['protocol']
                                )
                        # No Protocol
                        else:
                            if 'hdwallet' in network_yaml['development']:
                                __ = dict(
                                    url=network_yaml['development']['url']
                                )
                                hdwallet = self.hdwallet(network_yaml['development']['hdwallet'])
                                return {**__, **hdwallet}
                            elif 'account' in network_yaml['development']:
                                __ = dict(
                                    url=network_yaml['development']['url']
                                )
                                account = self.account(network_yaml['development']['account'])
                                return {**__, **account}
                            else:
                                return dict(
                                    url=network_yaml['development']['url']
                                )
            else:
                self.cobra_print("[ERROR] Cobra: There is no host/url in %s." % 'development',
                                 "error", bold=True)
                sys.exit()
        else:
            self.cobra_print("[ERROR] Cobra: There is no development in network.", "error", bold=True)
            sys.exit()
