from kgmk.twitter import (
  Request,
)

from . import (
  ByUsernameParams,
  ByIdParams,
  ByIdsParams,
  ByUsernamesParams,
)



class MakeRequest():
  def by_id(
    self,
    id_: str,
    params: ByIdParams,
  ) -> Request:
    api_path = (
      f'/2/users/{id_}'
    )
    return Request(
      api_path,
      params.to_dict(),
    )


  def by_ids(
    self,
    params: ByIdsParams,
  ) -> Request:
    api_path = '/2/users'
    return Request(
      api_path,
      params.to_dict(),
    )


  def by_username(
    self,
    username: str,
    params: ByUsernameParams,
  ) -> Request:
    api_path = (
      '/2/users/by/username/'
      f'{username}' 
    )
    return Request(
      api_path,
      params.to_dict(),
    )


  def by_usernames(
    self,
    params: ByUsernamesParams,
  ) -> Request:
    api_path = '/2/users/by'
    return Request(
      api_path,
      params.to_dict(),
    )
    