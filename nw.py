from __future__ import division 
import networkx as nx
import json
import matplotlib.pyplot as plt

def main(data):
    """docstring for main"""
    DG = nx.DiGraph()

    for item in json.loads(complex_data):
        DG.add_node(item['Id'], tags=item['RepoTags'])
        DG.add_node(item['ParentId'], tags=item['RepoTags'])
        DG.add_edge(item['ParentId'], item['Id'])
    return DG


def mpl(graph):
    fig = plt.figure(1,figsize=(16,16))

    ax = plt.axes()
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    top_node = graph.node['']
    top_edge = graph.edge['']

    number_of_nodes = len(graph.nodes())
    move_amount = 1/number_of_nodes


    for count, x in enumerate(nx.dfs_preorder_nodes(graph, '')):
        y = 1 - count * move_amount
        plt.text(.5,y,s=x[:5], bbox=dict(facecolor='red', alpha=0.2),horizontalalignment='center')

    plt.show()
    fig.savefig("test.png")



if __name__=="__main__":
    simple_data = """[{"Created":1421613815,"Id":"59838709c8282fb461f3a0337c2cf15a55401953cc5d0ea316f138f250af0021","ParentId":"5f3a622b9b1b4a992f5f5bcfe70430f440405b15a75f5cf37d418c903c7f086d","RepoTags":["wiseio/datascience-base:latest"],"Size":0,"VirtualSize":1399233594}
    ,{"Created":1421613097,"Id":"e3eb50754662af60e523df925ee518ba7d527310c3b3afe915a2a864dea1651e","ParentId":"3e845f2770e1fbcfb1352733b48f8ab77b4648d1643ddf6987d8cf1da99c9df1","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1551850,"VirtualSize":1316782756}
    ,{"Created":1421612534,"Id":"ed838667116b1bb2cef7c7423173a72b5a457a6539921d722e049ec3346c3722","ParentId":"68425347ea9012bb895b242a46475c3c173e659947eb07058b503a2ed4203eb4","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1369517,"VirtualSize":1247549061}
    ,{"Created":1421446840,"Id":"0fca0ab2af5f5e7a1c5259c4225f40844201289fd9751ac7fe1d750186d38892","ParentId":"2b2b00e9373f86efaecf1baaea6b15e11fcbb4cb5ed31065cef9441fd0c422cf","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1247518468}
    ,{"Created":1421443530,"Id":"b39b81afc8cae27d6fc7ea89584bad5e0ba792127597d02425eaee9f3aaaa462","ParentId":"615c102e2290b70d38d89c03a1ad263da8bd8b05fb7fc8479174e5fd2215520e","RepoTags":["ubuntu:latest","ubuntu:trusty","ubuntu:14.04","ubuntu:14.04.1"],"Size":0,"VirtualSize":188305056}
    ,{"Created":1420066679,"Id":"e45a5af57b00862e5ef5782a9925979a02ba2b12dff832fd0991335f4a11e5c5","ParentId":"31cbccb51277105ba3ae35ce33c22b69c9e3f1002e76e4c736a2e8ebff9d7b5d","RepoTags":["hello-world:latest"],"Size":0,"VirtualSize":910}
    ]"""

    complex_data = """
    [{"Created":1421613815,"Id":"5f3a622b9b1b4a992f5f5bcfe70430f440405b15a75f5cf37d418c903c7f086d","ParentId":"eb87f233ce8b40818507c52c1e3e57d01f081fd2a8fd409bcb6fc4746c6890d3","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1399233594}
    ,{"Created":1421613815,"Id":"eb87f233ce8b40818507c52c1e3e57d01f081fd2a8fd409bcb6fc4746c6890d3","ParentId":"2cff799bc2fc764e70d80ff6c3528a37112c60b7b797c43c44f60e463f090edb","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":920,"VirtualSize":1399233594}
    ,{"Created":1421613815,"Id":"59838709c8282fb461f3a0337c2cf15a55401953cc5d0ea316f138f250af0021","ParentId":"5f3a622b9b1b4a992f5f5bcfe70430f440405b15a75f5cf37d418c903c7f086d","RepoTags":["wiseio/datascience-base:latest"],"Size":0,"VirtualSize":1399233594}
    ,{"Created":1421613814,"Id":"33ac4466cb44751088fde25ead6165b457b431756b6719cce3873151e250672e","ParentId":"c2f3ae1eb807a943551965f881edbbe90f752c08487a1a7138673c3a5d00730e","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":5507,"VirtualSize":1399231754}
    ,{"Created":1421613814,"Id":"2cff799bc2fc764e70d80ff6c3528a37112c60b7b797c43c44f60e463f090edb","ParentId":"5d4ad53a0c71e01ea6b7d134fa414a04aed066acb3810360ea540b59b40ca441","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":920,"VirtualSize":1399232674}
    ,{"Created":1421613814,"Id":"5d4ad53a0c71e01ea6b7d134fa414a04aed066acb3810360ea540b59b40ca441","ParentId":"33ac4466cb44751088fde25ead6165b457b431756b6719cce3873151e250672e","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1399231754}
    ,{"Created":1421613813,"Id":"c2f3ae1eb807a943551965f881edbbe90f752c08487a1a7138673c3a5d00730e","ParentId":"3016a9ea06d6bb7c69776f7f381e4a2c2ba363d5af9aed827145bdd1390036ae","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1399226247}
    ,{"Created":1421613813,"Id":"640c8e1851b02569b2530d10fd089a4e6a4144839bfff708c6103f2e1587b353","ParentId":"db348857bc639f323aba7a3f0e2a8fee0fbaab36779f3edbc54e58cee461e246","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1399226247}
    ,{"Created":1421613813,"Id":"3016a9ea06d6bb7c69776f7f381e4a2c2ba363d5af9aed827145bdd1390036ae","ParentId":"640c8e1851b02569b2530d10fd089a4e6a4144839bfff708c6103f2e1587b353","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1399226247}
    ,{"Created":1421613812,"Id":"db348857bc639f323aba7a3f0e2a8fee0fbaab36779f3edbc54e58cee461e246","ParentId":"39b2c8b520b7eecdc99cb0c0d42c16679bd5222110dc4a58d939715e7b917ecf","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":14355281,"VirtualSize":1399226247}
    ,{"Created":1421613732,"Id":"39b2c8b520b7eecdc99cb0c0d42c16679bd5222110dc4a58d939715e7b917ecf","ParentId":"9af2de5d66b6e1942e114ba5c0c634e56dc814b89c7905822fe95d612fc13261","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1551849,"VirtualSize":1384870966}
    ,{"Created":1421613693,"Id":"9af2de5d66b6e1942e114ba5c0c634e56dc814b89c7905822fe95d612fc13261","ParentId":"b24f9af28624e78abec9989ff951e7e6144675fca9ed3c35bb5d6ab62471dbf8","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":911197319,"VirtualSize":1383319117}
    ,{"Created":1421613483,"Id":"b24f9af28624e78abec9989ff951e7e6144675fca9ed3c35bb5d6ab62471dbf8","ParentId":"cce09b33ccdf51aa8ab6d45dc36661db5be1378409960e9d5f4f4b42ad3269a8","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":472121798}
    ,{"Created":1421613482,"Id":"cce09b33ccdf51aa8ab6d45dc36661db5be1378409960e9d5f4f4b42ad3269a8","ParentId":"cab572b43927ab9a75c0ddb78248f5c0373d1bec18ac6528a49b91a88bc69f4b","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":2844682,"VirtualSize":472121798}
    ,{"Created":1421613481,"Id":"cab572b43927ab9a75c0ddb78248f5c0373d1bec18ac6528a49b91a88bc69f4b","ParentId":"fa3d85ac89b732a846f3578fe7b187fe0c532787fb7e14548932e8d76bb8322a","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":469277116}
    ,{"Created":1421613479,"Id":"fa3d85ac89b732a846f3578fe7b187fe0c532787fb7e14548932e8d76bb8322a","ParentId":"3253343c7d2827bcbf4e29e30a4b9e958c4bb452493c106b9c4be363c469508b","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":87345386,"VirtualSize":469277116}
    ,{"Created":1421613470,"Id":"3253343c7d2827bcbf4e29e30a4b9e958c4bb452493c106b9c4be363c469508b","ParentId":"57449b2b862421c7822ea9c454732f91d9cbb51c938426b46d83e8513fc45aa5","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":21739832,"VirtualSize":381931730}
    ,{"Created":1421613463,"Id":"57449b2b862421c7822ea9c454732f91d9cbb51c938426b46d83e8513fc45aa5","ParentId":"3e451cebdaf252411e2837b6e9556369a1ecfc6ed72d463cf0aa4cf1dd1783f8","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":34103,"VirtualSize":360191898}
    ,{"Created":1421613461,"Id":"3e451cebdaf252411e2837b6e9556369a1ecfc6ed72d463cf0aa4cf1dd1783f8","ParentId":"7221262938c5170854b5f32e599852389e98fa4c370c91df397842fcb70c3965","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1621258,"VirtualSize":360157795}
    ,{"Created":1421613460,"Id":"2f07211204c0d3977e82abf78e363473de3b95d17e73dd932f94a10c4464e9a3","ParentId":"7aa8ffc6a47cac99644ab95265deebfea25bb985987e0a29be44a8eb8f3d0c44","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":358536537}
    ,{"Created":1421613460,"Id":"7221262938c5170854b5f32e599852389e98fa4c370c91df397842fcb70c3965","ParentId":"2f07211204c0d3977e82abf78e363473de3b95d17e73dd932f94a10c4464e9a3","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":358536537}
    ,{"Created":1421613455,"Id":"7aa8ffc6a47cac99644ab95265deebfea25bb985987e0a29be44a8eb8f3d0c44","ParentId":"e1c1ada14caa215c992e33ec155aac4d629e9575df692c3b28b2dc10acfdc35b","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":170231481,"VirtualSize":358536537}
    ,{"Created":1421613097,"Id":"e3eb50754662af60e523df925ee518ba7d527310c3b3afe915a2a864dea1651e","ParentId":"3e845f2770e1fbcfb1352733b48f8ab77b4648d1643ddf6987d8cf1da99c9df1","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1551850,"VirtualSize":1316782756}
    ,{"Created":1421613062,"Id":"3e845f2770e1fbcfb1352733b48f8ab77b4648d1643ddf6987d8cf1da99c9df1","ParentId":"bccdf03d101fe3a1b6e6c40a67ba95477626acac628e03d898f4830710cba363","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":911197319,"VirtualSize":1315230906}
    ,{"Created":1421612737,"Id":"bccdf03d101fe3a1b6e6c40a67ba95477626acac628e03d898f4830710cba363","ParentId":"8c6f62920c92bf79a3577a2ddd608988761f08fd72520dfa83e06acd73127466","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":404033587}
    ,{"Created":1421612737,"Id":"8c6f62920c92bf79a3577a2ddd608988761f08fd72520dfa83e06acd73127466","ParentId":"6ddfb3169cd478151deb0a89a47d062bf7fb0791c091448d5aedd8838c25df8d","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":2844682,"VirtualSize":404033587}
    ,{"Created":1421612736,"Id":"6ddfb3169cd478151deb0a89a47d062bf7fb0791c091448d5aedd8838c25df8d","ParentId":"0a81283ef52c3215ca3884c14c4e1f84d2c46ba89ac8c13fd1180d9263da0510","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":401188905}
    ,{"Created":1421612732,"Id":"0a81283ef52c3215ca3884c14c4e1f84d2c46ba89ac8c13fd1180d9263da0510","ParentId":"71a4a608e69e85f857f6ae001ea79b2faaa34658f4c022b80f9dabea3668dd1f","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":87345386,"VirtualSize":401188905}
    ,{"Created":1421612719,"Id":"71a4a608e69e85f857f6ae001ea79b2faaa34658f4c022b80f9dabea3668dd1f","ParentId":"86d85c23120a294223b7ddacf473ec5305fc2309e18bae28a28ba9262130bcf0","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":21739832,"VirtualSize":313843519}
    ,{"Created":1421612704,"Id":"86d85c23120a294223b7ddacf473ec5305fc2309e18bae28a28ba9262130bcf0","ParentId":"33e9cf91b358e49fc022386964faf7a1cffdbf5516c665c610e0761e87a6e855","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":34103,"VirtualSize":292103687}
    ,{"Created":1421612703,"Id":"33e9cf91b358e49fc022386964faf7a1cffdbf5516c665c610e0761e87a6e855","ParentId":"e69a1dcccceb5b6787bfc353687844d5b4876a53a976e02eafc8625dbf8e182b","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1621258,"VirtualSize":292069584}
    ,{"Created":1421612702,"Id":"e69a1dcccceb5b6787bfc353687844d5b4876a53a976e02eafc8625dbf8e182b","ParentId":"92c07a2fb13b17eb8105a9667bb15ae728bb85441b091d2ae438549e6ed8b1d1","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":290448326}
    ,{"Created":1421612701,"Id":"92c07a2fb13b17eb8105a9667bb15ae728bb85441b091d2ae438549e6ed8b1d1","ParentId":"5253c37f002e6c4c15316aa6f6bf288a702d62f9af7e6e5bc82bda3f88e44071","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":290448326}
    ,{"Created":1421612698,"Id":"5253c37f002e6c4c15316aa6f6bf288a702d62f9af7e6e5bc82bda3f88e44071","ParentId":"e1c1ada14caa215c992e33ec155aac4d629e9575df692c3b28b2dc10acfdc35b","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":102143270,"VirtualSize":290448326}
    ,{"Created":1421612534,"Id":"ed838667116b1bb2cef7c7423173a72b5a457a6539921d722e049ec3346c3722","ParentId":"68425347ea9012bb895b242a46475c3c173e659947eb07058b503a2ed4203eb4","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1369517,"VirtualSize":1247549061}
    ,{"Created":1421612501,"Id":"68425347ea9012bb895b242a46475c3c173e659947eb07058b503a2ed4203eb4","ParentId":"7602d370b360b9a945545f9abe2bee33fe0f1fc2288c10215cc1486d408f2bd8","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":911197319,"VirtualSize":1246179544}
    ,{"Created":1421612270,"Id":"7602d370b360b9a945545f9abe2bee33fe0f1fc2288c10215cc1486d408f2bd8","ParentId":"e42c0d98acd27f89791115cdd8ec80c20e0a04bdce956b4842ac85dae95bae9f","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":334982225}
    ,{"Created":1421612270,"Id":"e42c0d98acd27f89791115cdd8ec80c20e0a04bdce956b4842ac85dae95bae9f","ParentId":"1cc5b6eca7b9ae50552f924ec650f735774e76c6c056e8bfc4567c216f554689","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":2844682,"VirtualSize":334982225}
    ,{"Created":1421612269,"Id":"1cc5b6eca7b9ae50552f924ec650f735774e76c6c056e8bfc4567c216f554689","ParentId":"49ae04f4ac292697fc996e9bb4a78a4375bbcbb5f9661647b5aa4b15c86a0d1f","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":332137543}
    ,{"Created":1421612267,"Id":"49ae04f4ac292697fc996e9bb4a78a4375bbcbb5f9661647b5aa4b15c86a0d1f","ParentId":"86a49a71496f21ca9eca8440e67569a5bfbaaae5ce0e022eefd60711887fd766","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":87345386,"VirtualSize":332137543}
    ,{"Created":1421612259,"Id":"86a49a71496f21ca9eca8440e67569a5bfbaaae5ce0e022eefd60711887fd766","ParentId":"627928260b5fa1b39730eb1735e98f451cb7b1bdb84c263a6bd0d28cb70cbdba","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":21739832,"VirtualSize":244792157}
    ,{"Created":1421612251,"Id":"627928260b5fa1b39730eb1735e98f451cb7b1bdb84c263a6bd0d28cb70cbdba","ParentId":"565afeecadf29a452b1e4f9222974f1170cb23315486d322ecd2ec424f8cdf34","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":34103,"VirtualSize":223052325}
    ,{"Created":1421612249,"Id":"565afeecadf29a452b1e4f9222974f1170cb23315486d322ecd2ec424f8cdf34","ParentId":"6e11459fd4a98b7f3659da6061d8ad7cf4a9fdb01c2f88b46240bbc03a3b6097","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1621258,"VirtualSize":223018222}
    ,{"Created":1421612248,"Id":"6e11459fd4a98b7f3659da6061d8ad7cf4a9fdb01c2f88b46240bbc03a3b6097","ParentId":"200b9751cfb2aa8df298321946684d03aac856dcd9931be3f45752b77f095539","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":221396964}
    ,{"Created":1421612248,"Id":"200b9751cfb2aa8df298321946684d03aac856dcd9931be3f45752b77f095539","ParentId":"e18041aa1194294dafc7e9bc588228de2daef716057d522b4b11b7bd1c96414d","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":221396964}
    ,{"Created":1421612246,"Id":"e18041aa1194294dafc7e9bc588228de2daef716057d522b4b11b7bd1c96414d","ParentId":"e1c1ada14caa215c992e33ec155aac4d629e9575df692c3b28b2dc10acfdc35b","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":33091908,"VirtualSize":221396964}
    ,{"Created":1421612188,"Id":"4857f2af478f0c2b174a60afb4da8a48a6ebeb2975721786a6fc6d9bb836b1d7","ParentId":"b39b81afc8cae27d6fc7ea89584bad5e0ba792127597d02425eaee9f3aaaa462","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":188305056}
    ,{"Created":1421612188,"Id":"e1c1ada14caa215c992e33ec155aac4d629e9575df692c3b28b2dc10acfdc35b","ParentId":"4857f2af478f0c2b174a60afb4da8a48a6ebeb2975721786a6fc6d9bb836b1d7","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":188305056}
    ,{"Created":1421446840,"Id":"0fca0ab2af5f5e7a1c5259c4225f40844201289fd9751ac7fe1d750186d38892","ParentId":"2b2b00e9373f86efaecf1baaea6b15e11fcbb4cb5ed31065cef9441fd0c422cf","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1247518468}
    ,{"Created":1421446839,"Id":"5a1a0550fb4d82b806ae57f3aacdd871fdea3b101679780764b56aa79d299669","ParentId":"4210a5f791bac1ea4b02933b104678f7f2e1c434bdb026c29d3527df5471ac6a","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":920,"VirtualSize":1247517548}
    ,{"Created":1421446839,"Id":"2b2b00e9373f86efaecf1baaea6b15e11fcbb4cb5ed31065cef9441fd0c422cf","ParentId":"037286aece31010afdf943e1536b2f5ec3d548048e52f9553577dec50d112348","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1247518468}
    ,{"Created":1421446839,"Id":"037286aece31010afdf943e1536b2f5ec3d548048e52f9553577dec50d112348","ParentId":"5a1a0550fb4d82b806ae57f3aacdd871fdea3b101679780764b56aa79d299669","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":920,"VirtualSize":1247518468}
    ,{"Created":1421446838,"Id":"878c339a44dc04c719f450808c43cb41654fdcdb4cfb2b83bbddcbb7cb2c9555","ParentId":"cd9f8d8018e53844abbe1c6a4cf9e0e54737be26d601255e672fee111952ab2f","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":5432,"VirtualSize":1247516628}
    ,{"Created":1421446838,"Id":"4210a5f791bac1ea4b02933b104678f7f2e1c434bdb026c29d3527df5471ac6a","ParentId":"878c339a44dc04c719f450808c43cb41654fdcdb4cfb2b83bbddcbb7cb2c9555","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1247516628}
    ,{"Created":1421446838,"Id":"cd9f8d8018e53844abbe1c6a4cf9e0e54737be26d601255e672fee111952ab2f","ParentId":"372dbcd93da0166b2bd9e5ccfc5e2ca2de3128ea79d09798f6dad6e72d07b0bc","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1247511196}
    ,{"Created":1421444290,"Id":"372dbcd93da0166b2bd9e5ccfc5e2ca2de3128ea79d09798f6dad6e72d07b0bc","ParentId":"08502343a6e5ea76b32e02b93aef5f657421e24cbeca335ac2970ed00ee25961","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1247511196}
    ,{"Created":1421444289,"Id":"08502343a6e5ea76b32e02b93aef5f657421e24cbeca335ac2970ed00ee25961","ParentId":"26fdf905152ae55d4254e63f332c404986b5ae966c66e3bd82a37b4a0ba91ff2","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":1247511196}
    ,{"Created":1421443786,"Id":"26fdf905152ae55d4254e63f332c404986b5ae966c66e3bd82a37b4a0ba91ff2","ParentId":"4406df957ba8215d463131526c5f577f292416ac880ad65ff41683e6b4192abd","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1369520,"VirtualSize":1247511196}
    ,{"Created":1421443754,"Id":"4406df957ba8215d463131526c5f577f292416ac880ad65ff41683e6b4192abd","ParentId":"4887420ae2f067f5e4ca5da43e83f42ee103a8ad9bbbe8a24fc89c79155a7992","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":911197319,"VirtualSize":1246141676}
    ,{"Created":1421443554,"Id":"4887420ae2f067f5e4ca5da43e83f42ee103a8ad9bbbe8a24fc89c79155a7992","ParentId":"dc4b5d46d6cd98f41b47698d00e2de2f443fdf4be7223120fe31269d78cef9ae","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":334944357}
    ,{"Created":1421443553,"Id":"66642aeaa73c38336982f1fa0c7e86bb444c2ec5498d6462961db9b57607ab1d","ParentId":"051be630a9fc24bb0a28a065af6550034a165232fe4564f0a0268a4176fa5489","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":332114305}
    ,{"Created":1421443553,"Id":"dc4b5d46d6cd98f41b47698d00e2de2f443fdf4be7223120fe31269d78cef9ae","ParentId":"66642aeaa73c38336982f1fa0c7e86bb444c2ec5498d6462961db9b57607ab1d","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":2830052,"VirtualSize":334944357}
    ,{"Created":1421443551,"Id":"051be630a9fc24bb0a28a065af6550034a165232fe4564f0a0268a4176fa5489","ParentId":"4e1bfdaec0768f23bb9228c1697434a51b89be1f3cc112b5dcddcc4ce7358d40","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":87345386,"VirtualSize":332114305}
    ,{"Created":1421443544,"Id":"4e1bfdaec0768f23bb9228c1697434a51b89be1f3cc112b5dcddcc4ce7358d40","ParentId":"bb3322bfd79562a24f735d212d571e3d4732ffcb621068df4e75594275166254","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":21739832,"VirtualSize":244768919}
    ,{"Created":1421443536,"Id":"bb3322bfd79562a24f735d212d571e3d4732ffcb621068df4e75594275166254","ParentId":"a9e1847c98bbed2087268cb4717fab03c1ad602f59291d220150fdc9053d6922","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":34103,"VirtualSize":223029087}
    ,{"Created":1421443535,"Id":"a9e1847c98bbed2087268cb4717fab03c1ad602f59291d220150fdc9053d6922","ParentId":"28141f7a963dc238434b2b70d21780fda7179bb06ac040d532b3bf881786ad16","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1621258,"VirtualSize":222994984}
    ,{"Created":1421443533,"Id":"2a50747b97a61dbf90e645c43b4d3ebfc1ddb65b5b074ba0849bc9f3fb467a42","ParentId":"431fe85cbacca137e04fe0af97a7abcaaec91b622fa254c5f18b7a70b042c28e","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":221373726}
    ,{"Created":1421443533,"Id":"28141f7a963dc238434b2b70d21780fda7179bb06ac040d532b3bf881786ad16","ParentId":"2a50747b97a61dbf90e645c43b4d3ebfc1ddb65b5b074ba0849bc9f3fb467a42","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":221373726}
    ,{"Created":1421443532,"Id":"431fe85cbacca137e04fe0af97a7abcaaec91b622fa254c5f18b7a70b042c28e","ParentId":"65573b84eeb53ce1c6c9bf856019688baf9b7583779691ab8b4256b2e9e2229d","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":33074607,"VirtualSize":221373726}
    ,{"Created":1421443530,"Id":"b39b81afc8cae27d6fc7ea89584bad5e0ba792127597d02425eaee9f3aaaa462","ParentId":"615c102e2290b70d38d89c03a1ad263da8bd8b05fb7fc8479174e5fd2215520e","RepoTags":["ubuntu:14.04","ubuntu:14.04.1","ubuntu:latest","ubuntu:trusty"],"Size":0,"VirtualSize":188305056}
    ,{"Created":1421443528,"Id":"615c102e2290b70d38d89c03a1ad263da8bd8b05fb7fc8479174e5fd2215520e","ParentId":"837339b915388417a842c87a681a5448df2509068c8d3efd1638f1fad2eacea2","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1895,"VirtualSize":188305056}
    ,{"Created":1421443526,"Id":"837339b915388417a842c87a681a5448df2509068c8d3efd1638f1fad2eacea2","ParentId":"53f858aaaf03033e088d357df23e311d71aa93ac578ef39aa8230580ea95076f","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":194533,"VirtualSize":188303161}
    ,{"Created":1421443521,"Id":"53f858aaaf03033e088d357df23e311d71aa93ac578ef39aa8230580ea95076f","ParentId":"511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":188108628,"VirtualSize":188108628}
    ,{"Created":1421443490,"Id":"dde06b81fbb5fce861687da99cdfec2893a6b395ab2714b179354f81c8b824f6","ParentId":"8eaa4ff06b53ff7730c4d7a7e21b4426a4b46dee064ca2d5d90d757dc7ea040a","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":188299119}
    ,{"Created":1421443490,"Id":"65573b84eeb53ce1c6c9bf856019688baf9b7583779691ab8b4256b2e9e2229d","ParentId":"dde06b81fbb5fce861687da99cdfec2893a6b395ab2714b179354f81c8b824f6","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":188299119}
    ,{"Created":1420075526,"Id":"8eaa4ff06b53ff7730c4d7a7e21b4426a4b46dee064ca2d5d90d757dc7ea040a","ParentId":"f62feddc05dc67da9b725361f97d7ae72a32e355ce1585f9a60d090289120f73","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":188299119}
    ,{"Created":1420075525,"Id":"f62feddc05dc67da9b725361f97d7ae72a32e355ce1585f9a60d090289120f73","ParentId":"607c5d1cca71dd3b6c04327c3903363079b72ab3e5e4289d74fb00a9ac7ec2aa","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":1895,"VirtualSize":188299119}
    ,{"Created":1420075524,"Id":"607c5d1cca71dd3b6c04327c3903363079b72ab3e5e4289d74fb00a9ac7ec2aa","ParentId":"3b363fd9d7dab4db9591058a3f43e806f6fa6f7e2744b63b2df4b84eadb0685a","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":194533,"VirtualSize":188297224}
    ,{"Created":1420075518,"Id":"3b363fd9d7dab4db9591058a3f43e806f6fa6f7e2744b63b2df4b84eadb0685a","ParentId":"511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":188102691,"VirtualSize":188102691}
    ,{"Created":1420066679,"Id":"e45a5af57b00862e5ef5782a9925979a02ba2b12dff832fd0991335f4a11e5c5","ParentId":"31cbccb51277105ba3ae35ce33c22b69c9e3f1002e76e4c736a2e8ebff9d7b5d","RepoTags":["hello-world:latest"],"Size":0,"VirtualSize":910}
    ,{"Created":1420066678,"Id":"31cbccb51277105ba3ae35ce33c22b69c9e3f1002e76e4c736a2e8ebff9d7b5d","ParentId":"511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":910,"VirtualSize":910}
    ,{"Created":1371157430,"Id":"511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158","ParentId":"","RepoTags":["\u003cnone\u003e:\u003cnone\u003e"],"Size":0,"VirtualSize":0}
    ]"""
    mpl(main(complex_data))

