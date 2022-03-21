import time


class TestRunner(object):
    @staticmethod
    def run(runnables, test_data):
        results = []
        for i, td in enumerate(test_data):
            results.append([])
            for j, runnable in enumerate(runnables):
                start = time.time()

                res = runnable(*td)
                end = time.time()
                print("Solution name: %s. Completed test #%s, Runtime: %s, res: %s" % (str(runnable).split(' ')[1], str(i), str(end - start), str(res)))
                results[i].append(res)
        return results
