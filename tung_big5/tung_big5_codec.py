import codecs


class TungBig5Codec(codecs.Codec):
    #...

    def encode(self, string: str, errors='strict'):
        output = bytearray()
        for char in string:
            # output.extend(convert_unicode_to_big5_eudc(char))
            pass
        return bytes(output), len(string)

    def decode(self, string, errors='strict'):
        output = ''
        i = 0
        while i < len(string):
            # hex_code = string[i:i + 2]
            # output += convert_eudc_big5_to_unicode(hex_code)
            pass
        return output, len(output)


def tung_big5_search_func(encoding):
    if encoding == 'tung_big5':
        handler = TungBig5Codec()
        return codecs.CodecInfo(
            name='tung_big5',
            encode=handler.encode,
            decode=handler.decode
        )


codecs.register(tung_big5_search_func)  # 註冊 codec