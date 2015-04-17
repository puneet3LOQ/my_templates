#/home/puneet/workspace/folder_monitor.py
'''
Platform independent file system monitor.
'''
from __future__ import nested_scopes

import os, time

def watch_directories(paths, func, delay=0.1):
    '''
    Watches a list of directories specified in 'paths' and runs func on each
    new/changed file encountered in paths. Func can return True/False. If it
    returns True, the paths are immediately rescanned without applying func.
    This is for use with functions which may make changes which affect files 
    in 'paths'. 
    @param
    paths (list) - A list of unix paths to monitor.
    func (function) - Function variable to call on each new/changed file
                        found in paths.
    delay (float) - Wait time between scans on paths.
    @return
    None
    '''
    
    ##Dict to map files to modification time.
    all_files = {}
    def f(unused, dirname, files):
        for filename in files:
            path = os.path.join(dirname, filename)
            try:
                t = os.stat(path)
            except os.error:
                continue
            mtime = remaining_files.get(path)
            if mtime is not None:
                del remaining_files[path]
                if t.st_mtime > mtime:
                    changed_list.append(path)
            else:
                changed_list.append(path)
            all_files[path] = t.st_mtime
            
    rescan = False
    while True:
        changed_list = []
        remaining_files = all_files.copy()
        all_files = {}
        for path in paths:
            os.path.walk(path, f, None)
        removed_list = remaining_files.keys()
        if rescan:
            rescan = False
        elif changed_list or removed_list:
            rescan = func(changed_list, removed_list)
        
        time.sleep(delay)


if __name__ == '__main__':
    def f(changed_files, removed_files):
        print changed_files
        print 'Removed: ', removed_files
        
    watch_directories(['.'], f, delay=5)
    
    
    
    