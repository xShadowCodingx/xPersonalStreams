# xPersonal Streams

Personal cloud streaming service software built in Python.

**Outline:**

#### API
- **/**
- - GET: Login
- **/users**
- - GET: User information
- - POST: Create User
- - DEL: Delete User
- - PUT: Edit User
- **/permissions**
- - GET: User Permissions
- - POST: Create Permissions
- - DEL: Delete Permissions
- - PUT: Edit Permissions
- **/media**
- - GET: All Media
- **/media/videos**
- - GET: All Videos
- **/media/video**
- - GET: Video By ID
- - POST: Create New Video Log And Save Video
- - DEL: Delete Video Log
- - PUT: Edit Video Log
- **/media/video/newest**
- - GET: Latest 10 Videos
- **/media/video/popular**
- - GET: 10 Most Watched Videos
- **/media/audios**
- - GET: All Audios
- **/media/audio**
- - GET: Audio By ID
- - POST: Create New Audio Log And Save Audio
- - DEL: Delete Audio Log
- - PUT: Edit Audio Log
- **/media/audio/newest**
- - GET: Latest 10 Audios
- **/media/audio/popular**
- - GET: 10 Most Played Audios
- **/media/images**
- - GET: All Images
- **/media/image**
- - GET: Image By ID
- - POST: Create New Image Log And Save Image
- - DEL: Delete Audio Log
- - PUT: Edit Audio Log
- **/media/image/newest**
- - GET: Latest 10 Images
- **/media/image/popular**
- - GET: 10 Most Viewed Images
- **/media/playlists**
- - GET: All Playlists
- **/media/playlist**
- - GET: Playlist By ID
- - POST: Create New Playlist (By Type)
- - DEL: Delete Playlist
- - PUT: Edit Playlist
- **/media/playlist/newest**
- - GET: 3 Newest Playlists
- **/media/playlist/popular**
- - GET: 5 Most Accessed Playlists