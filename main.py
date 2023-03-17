from fastapi import FastAPI, HTTPException,status
from models import Post


app = FastAPI()

posts = {
    1: {
    'titulo':'Post Um'
    },
    2: {
    'titulo' : 'Post Dois'
    }
}

@app.get('/posts/')
async def listar_posts():
    return posts

@app.get('/posts/{post_id}')
async def detalhar_posts(post_id:int):
    try:
        post = posts[post_id]
        return post
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail = 'Post inexistente.')

@app.post('/posts/', status_code=status.HTTP_201_CREATED)
async def post_curso(post: Post):
   id = len(posts) + 1
   posts[id] = post
   return posts

@app.delete('/posts/{post_id}')
def deletar_post(post_id : int): 
    try:
        del posts[post_id]
        return {"msg":"post deletado"}
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail = 'Post inexistente.')
@app.put('/posts/{post_id}')
def atualizar_post(post_id : int, post: Post):
    posts[post_id] = post
    return{"msg" : " post atualizado"}
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",
                host ="0.0.0.0",
                port=8000,
                reload=True
                )

