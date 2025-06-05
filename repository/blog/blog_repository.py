from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from model.blog.request.BlogBaseRequest import BlogBaseRequest
from model.blog.request.BlogWithUserRequest import BlogWithUserRequest
from schema.blog.BlogTable import Blog


def get_all(db: Session):
    blogs = db.query(Blog).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Something went wrong!"
        )
    return blogs


def show_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found."
        )
    return blog


def create_blog(request: BlogWithUserRequest, db: Session):
    blog = Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def update_blog(id: int, request: BlogBaseRequest, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found."
        )
    blog.update(dict(request))
    db.commit()
    return {"detail": "blog updated successfully."}


def delete_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found."
        )
    db.delete(blog)
    db.commit()
    return {"detail": "Blog deleted successfully."}
